"""Create web-ready hero videos and small first-frame posters; retain originals."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools/media'))
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
for name in ('video1', 'video3'):
    source = ROOT / 'videos' / f'{name}.mp4'
    target = ROOT / 'videos' / f'{name}-optimized.mp4'
    subprocess.run([ffmpeg, '-y', '-i', str(source), '-an', '-vf', "scale='min(1280,iw)':-2,fps=24", '-c:v', 'libx264', '-preset', 'slow', '-crf', '28', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(target)], check=True, capture_output=True)
    subprocess.run([ffmpeg, '-y', '-i', str(target), '-frames:v', '1', '-update', '1', '-quality', '78', str(ROOT / 'images' / f'{name}-poster.webp')], check=True, capture_output=True)
    print(f'{source.name}: {source.stat().st_size:,} -> {target.stat().st_size:,} bytes', flush=True)
