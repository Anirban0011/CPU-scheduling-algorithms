import ctypes
from typing import List
from fastapi import FastAPI, Form

app = FastAPI(title="cpu-scheduler-app")

clib = ctypes.CDLL('./c_file.so')

class Process(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_int),
        ("at", ctypes.c_int),
        ("ct", ctypes.c_int),
        ("wt", ctypes.c_int),
        ("tat", ctypes.c_int),
        ("burst", ctypes.c_int),
        ("rt", ctypes.c_int),
        ("priority", ctypes.c_int),
    ]

@app.get("/")
async def root():
    return {"status": "ok", "message": "Space is running"}

@app.post("/fcfs")
async def fcfs(ats : List[int] = Form(...),
               bursts : List[int] = Form(...),
               prts : List[int] = Form(...)
               ):
    clib.FCFS.argtypes = (ctypes.POINTER(Process), ctypes.c_int)
    clib.FCFS.restype = None
    n = len(ats)
    arr = (Process*n)()

    for i in range(n):
        arr[i].id = i
        arr[i].at = ats[i]
        arr[i].burst = bursts[i]
        arr[i].priority = prts[i]

    clib.call_FCFS(arr, n)

    result = []
    for p in arr:
        result.append({
            "id": p.id,
            "at": p.at,
            "burst": p.burst,
            "priority": p.priority,
            "ct": p.ct,
            "wt": p.wt,
            "tat": p.tat,
            "rt": p.rt,
        })

    return {"result": result}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7860)

