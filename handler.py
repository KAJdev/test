import runpod

def handler(job):
  print(job)
  return job

runpod.serverless.start({"handler": handler})
