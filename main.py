from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI App — Muhammad Afnan Khan</title>
        <style>
            body { font-family: sans-serif; background: #0f1117;
                   color: #e2e8f0; display: flex; align-items: center;
                   justify-content: center; height: 100vh; margin: 0; }
            .box { background: #1e2330; border: 1px solid #2a3044;
                   border-radius: 16px; padding: 40px 50px; text-align: center; }
            h1 { color: #4ade80; margin-bottom: 8px; }
            p  { color: #94a3b8; }
            .badge { display: inline-block; background: #166534;
                     color: #4ade80; border-radius: 20px;
                     padding: 4px 14px; font-size: 13px; margin-top: 16px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>FastAPI Dashboard</h1>
            <p>Framework: FastAPI </p>
        
            <p>Deployed by Muhammad Afnan Khan</p>
            <div class="badge">Running</div>
        </div>
    </body>
    </html>
    """

@app.get("/api/info")
async def info():
    return {
        "framework": "FastAPI",
        "deployed_by": "Muhammad Afnan Khan",
        "status": "running"
    }