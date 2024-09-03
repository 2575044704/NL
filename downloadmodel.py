from huggingface_hub import snapshot_download

snapshot_download(repo_id="OpenGVLab/InternVL2-40B-AWQ", local_dir="models/model")
