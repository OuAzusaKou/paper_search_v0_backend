from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟搜索功能
def mock_search(query, source):
    # 这里可以替换为实际的数据库查询或外部API调用
    return [
        {'id': '1', 'title': 'Sample Paper 1', 'authors': 'Author A, Author B', 'abstract': 'This is a sample abstract...', 'source': source},
        {'id': '2', 'title': 'Sample Paper 2', 'authors': 'Author C, Author D', 'abstract': 'This is another sample abstract...', 'source': source},
    ]

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    source = request.args.get('source', 'all')
    results = mock_search(query, source)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)