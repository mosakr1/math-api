from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        # ⚠️ استخدام eval للتبسيط (غير آمن في الواقع)
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
