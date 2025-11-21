import logging
from flask import Flask, request, jsonify, render_template
import search_logic

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    print("Reached the search route")
    keyword = request.args.get('keyword')
    print(f"Keyword: {keyword}")

    video_files = ["C:/Users/91990/OneDrive/Desktop/Project/videos/v001.mp4"]
    srt_files = ["C:/Users/91990/OneDrive/Desktop/Project/videos/v001.srt"]

    try:
        results = search_logic.search_keyword_in_videos(keyword, video_files, srt_files)
        print(results)
        return jsonify(results)  # Return JSON response
    except Exception as e:
        logging.error(f"Error occurred during search: {e}")
        return jsonify({'error': 'An error occurred during search'}), 500

@app.route('/ans.html')
def ans():
    return render_template('ans.html')

if __name__ == '__main__':
    app.run(debug=True)
