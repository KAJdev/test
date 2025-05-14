import runpod

def handler(job):
  print(job)
  return job["input"]["text"]

runpod.serverless.start({"handler": handler})
