from utils import read_video, save_video
from trackers import PlayerTracker, BallTracker
from drawers import PlayerTracksDrawer, BallTracksDrawer

def main():

    # Read Video
    video_frames = read_video("input_videos/video_1.mp4")

    # Initialize Player and Ball Tracker
    player_tracker = PlayerTracker("models/player_detector.pt")
    ball_tracker = BallTracker("models/ball_detector.pt")

    # Track Players
    player_tracks = player_tracker.track_players(video_frames, read_from_stub=True, 
                                                 stub_path="stubs/player_tracks.pkl")

    ball_tracks = ball_tracker.track_ball(video_frames, read_from_stub=True, 
                                           stub_path="stubs/ball_tracks.pkl")

    # Remove Wrong Detections of the Ball
    ball_tracks = ball_tracker.remove_wrong_detection(ball_tracks)

    # Interpolation of the Ball
    ball_tracks = ball_tracker.ball_interpolation(ball_tracks)

    # Initialize Player Tracks Drawer
    player_tracks_drawer = PlayerTracksDrawer()

    # Initialize Ball Tracks Drawer
    ball_tracks_drawer = BallTracksDrawer()

    # Draw Player Tracks
    output_video_frames = player_tracks_drawer.draw(video_frames, player_tracks)

    # Draw Ball Tracks
    output_video_frames = ball_tracks_drawer.draw(output_video_frames, ball_tracks)

    # Save Video
    save_video(output_video_frames, "output_videos/output_video.mp4")
    
if __name__ == "__main__":
    main()