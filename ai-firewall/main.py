from fastapi import FastAPI, Request
from scapy.all import Ether
from ai_engine.engine import predict_packet_threat
from data_pipeline.parser import extract_features
from policy_engine.policy import evaluate_policy
from response_engine.handler import respond
from config.settings import settings
from dashboard_ui import router as dashboard_router
app.include_router(dashboard_router)


app = FastAPI(title=settings.app_name)
detector = TrafficAnomalyDetector()

@app.on_event("startup")
def startup():
    logger.info("AI Firewall starting up...")
    # Optional: Load or train model with historical data


@app.post("/analyze")
async def analyze_packet(packet_raw: bytes):
    packet = Ether(packet_raw)
    features = extract_features(packet)
    threat_score = predict_packet_threat(features)
    decision = evaluate_policy(threat_score)
    respond(decision, features)
    return {"decision": decision, "score": threat_score}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/detect")
def detect_traffic(features: list[float]):
    result = detector.detect([features])
    return {"anomaly": bool(result[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)