import subprocess, os

def generate_thumbnail(filepath, output_path=None, timestamp='00:00:05', size='320x180'):
    if output_path is None:
        output_path = os.path.splitext(filepath)[0] + '_thumb.jpg'
    cmd = ['ffmpeg', '-y', '-ss', timestamp, '-i', filepath,
           '-vframes', '1', '-s', size, '-q:v', '2', output_path]
    subprocess.run(cmd, capture_output=True, check=True)
    return output_path
