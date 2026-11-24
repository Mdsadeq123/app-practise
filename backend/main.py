from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "pulsecheck-backend"}


def calc_uptime_percent(up_checks: int, total_checks: int) -> float:
    if total_checks <= 0:
        return 0.0
    return round((up_checks / total_checks) * 100, 2)


@app.get("/uptime/{up}/{total}")
def uptime(up: int, total: int):
    return {"uptime_percent": calc_uptime_percent(up, total)}