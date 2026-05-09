import subprocess, os

def generate_thumbnail(filepath, output_path=None, timestamp='00:00:05', size='320x180'):
    """Generate a thumbnail from video at given timestamp."""
    if output_path is None:
        base = os.path.splitext(filepath)[0]
        output_path = f'{base}_thumb.jpg'
    cmd = ['ffmpeg', '-y', '-ss', timestamp, '-i', filepath,
           '-vframes', '1', '-s', size, '-q:v', '2', output_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f'ffmpeg failed: {result.stderr}')
    return output_path

def generate_gif_preview(filepath, output_path=None, start='00:00:02', duration=3):
    """Generate an animated GIF preview."""
    if output_path is None:
        base = os.path.splitext(filepath)[0]
        output_path = f'{base}_preview.gif'
    cmd = ['ffmpeg', '-y', '-ss', start, '-t', str(duration), '-i', filepath,
           '-vf', 'fps=10,scale=320:-1:flags=lanczos', output_path]
    subprocess.run(cmd, capture_output=True, check=True)
    return output_path
