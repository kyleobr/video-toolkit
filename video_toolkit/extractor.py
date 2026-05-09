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
    video_stream = next((s for s in streams if s['codec_type'] == 'video'), None)
    return {
        'duration': float(fmt.get('duration', 0)),
        'size_bytes': int(fmt.get('size', 0)),
        'bitrate': int(fmt.get('bit_rate', 0)),
        'width': video_stream.get('width') if video_stream else None,
        'height': video_stream.get('height') if video_stream else None,
        'codec': video_stream.get('codec_name') if video_stream else None,
    }
