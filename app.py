from flask import Flask, request, render_template
import os
from algorithms import kmp, boyer_moore, rabin_karp
from utils.performance import measure_performance
from utils.pdf_reader import extract_text_from_pdf
from utils.docx_reader import extract_text_from_docx

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_lines_with_matches(text, match_indexes, keywords):
    lines = text.split('\n')
    result_lines = []
    for line in lines:
        if any(keyword.lower() in line.lower() for keyword in keywords):
            result_lines.append(line)
    return list(set(result_lines))

@app.route('/', methods=['GET', 'POST'])
def index():
    algorithm_results = []
    preview_lines = []
    document_text = ''
    error = None
    file_name = ''
    keywords = []
    unmatched_keywords = []
    fastest_algorithm = None
    least_memory_algorithm = None

    if request.method == 'POST':
        file = request.files['document']
        pattern_input = request.form['pattern']

        if not file or not allowed_file(file.filename):
            error = "Only .txt, .pdf, and .docx files are supported."
            return render_template('index.html', algorithm_results=None, preview_lines=[], error=error)

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(file_path)

        file_name = file.filename

        ext = file.filename.rsplit('.', 1)[1].lower()
        if ext == 'txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                document_text = f.read()
        elif ext == 'pdf':
            document_text = extract_text_from_pdf(file_path)
        elif ext == 'docx':
            document_text = extract_text_from_docx(file_path)

        keywords = [kw.strip() for kw in pattern_input.split(',') if kw.strip()]
        match_indexes = {keyword: [] for keyword in keywords}

        algorithms = {
            'Knuth-Morris-Pratt': kmp.kmp_search,
            'Boyer-Moore': boyer_moore.boyer_moore_search,
            'Rabin-Karp': rabin_karp.rabin_karp_search,
        }

        for name, algo in algorithms.items():
            combined_matches = []
            for keyword in keywords:
                result = measure_performance(algo, document_text, keyword)
                combined_matches.extend([(keyword, m) for m in result['matches']])
                match_indexes[keyword].extend(result['matches'])
            algorithm_results.append({
                'name': name,
                'matches': combined_matches,
                'time': result['time'],
                'memory': result['memory']
            })

        # Find unmatched keywords
        unmatched_keywords = [kw for kw in keywords if len(match_indexes[kw]) == 0]

        preview_lines = get_lines_with_matches(document_text, match_indexes, keywords)

        # Find fastest & least memory algorithms
        fastest_algorithm = min(algorithm_results, key=lambda x: x['time'], default=None)
        least_memory_algorithm = min(algorithm_results, key=lambda x: x['memory'], default=None)

    return render_template(
        'index.html',
        algorithm_results=algorithm_results,
        preview_lines=preview_lines,
        error=error,
        file_name=file_name,
        keywords=keywords,
        fastest_algorithm=fastest_algorithm,
        least_memory_algorithm=least_memory_algorithm,
        unmatched_keywords=unmatched_keywords
    )

if __name__ == '__main__':
    app.run(debug=True)
