import subprocess, json

def extract_metadata(filepath):
    """Extract video metadata using ffprobe."""
    cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json',
           '-show_format', '-show_streams', filepath]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f'ffprobe failed: {result.stderr}')
    data = json.loads(result.stdout)
    fmt = data.get('format', {})
    streams = data.get('streams', [])
    vs = next((s for s in streams if s['codec_type'] == 'video'), None)
    return {
        'duration': float(fmt.get('duration', 0)),
        'size_bytes': int(fmt.get('size', 0)),
        'width': vs.get('width') if vs else None,
        'height': vs.get('height') if vs else None,
        'codec': vs.get('codec_name') if vs else None,
    }
