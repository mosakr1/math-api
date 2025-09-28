from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Math API is running ✅"

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json() or {}
    expression = data.get("expression", "")
    try:
        # ⚠️ استخدام eval للتبسيط — للاختبارات فقط، لا تقبل مدخلات مجهولة في الإنتاج
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # تأكد إن هذا البورت يطابق الـ docker run اللي بتستخدمه
    app.run(host="0.0.0.0", port=8000)
