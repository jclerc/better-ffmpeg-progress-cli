import sys
from better_ffmpeg_progress import FfmpegProcess

# Pass a list of FFmpeg arguments, like you would if using subprocess.run()
process = FfmpegProcess(sys.argv[1:], print_detected_duration=False)
# Use the run method to run the FFmpeg command.
process.run(
	progress_bar_description=process._input_filepath.name,
	log_file=f"{process._input_filepath.name}.log",
)

process._ffmpeg_log_file.unlink()
