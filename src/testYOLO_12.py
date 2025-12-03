import cv2
from ultralytics import YOLO
import time

def run_realtime_detection(model_path, conf_threshold=0.25, camera_id=0):
    """
    Run real-time object detection using YOLOv12 weights
    
    Args:
        model_path: Path to your .pt weights file
        conf_threshold: Confidence threshold for detections (0-1)
        camera_id: Camera ID (0 for default webcam)
    """
    
    # Load the model
    print(f"Loading model from {model_path}...")
    model = YOLO(model_path)
    print("Model loaded successfully!")
    
    # Open webcam
    cap = cv2.VideoCapture(camera_id)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    # Set camera properties for better performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # FPS calculation variables
    prev_time = 0
    
    print("Starting real-time detection... Press 'q' to quit")
    
    while True:
        # Read frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame")
            break
        
        # Run inference
        results = model.predict(frame, conf=conf_threshold, verbose=False)
        
        # Get annotated frame
        annotated_frame = results[0].plot()
        
        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time > 0 else 0
        prev_time = current_time
        
        # Add FPS to frame
        cv2.putText(annotated_frame, f'FPS: {fps:.1f}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display detection count
        num_detections = len(results[0].boxes)
        cv2.putText(annotated_frame, f'Detections: {num_detections}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Show frame
        cv2.imshow('YOLOv12 Real-time Detection', annotated_frame)
        
        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("Detection stopped")


def run_with_options(model_path):
    """
    Interactive version with adjustable settings
    """
    print("\n=== YOLOv12 Real-time Detection ===")
    print("Controls:")
    print("  'q' - Quit")
    print("  's' - Save current frame")
    print("  '+' - Increase confidence threshold")
    print("  '-' - Decrease confidence threshold")
    print()
    
    # Load model
    model = YOLO(model_path)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    conf_threshold = 0.25
    prev_time = 0
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Run inference
        results = model.predict(frame, conf=conf_threshold, verbose=False)
        annotated_frame = results[0].plot()
        
        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time > 0 else 0
        prev_time = current_time
        
        # Add info overlay
        cv2.putText(annotated_frame, f'FPS: {fps:.1f}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(annotated_frame, f'Conf: {conf_threshold:.2f}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(annotated_frame, f'Detections: {len(results[0].boxes)}', (10, 110),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('YOLOv12 Real-time Detection', annotated_frame)
        
        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('s'):
            filename = f'detection_{frame_count}.jpg'
            cv2.imwrite(filename, annotated_frame)
            print(f"Saved {filename}")
            frame_count += 1
        elif key == ord('+') or key == ord('='):
            conf_threshold = min(0.95, conf_threshold + 0.05)
            print(f"Confidence threshold: {conf_threshold:.2f}")
        elif key == ord('-') or key == ord('_'):
            conf_threshold = max(0.05, conf_threshold - 0.05)
            print(f"Confidence threshold: {conf_threshold:.2f}")
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # REPLACE THIS with your actual model path
    MODEL_PATH = "../models/Luis(Yolov11-7k).pt"
    
    # Simple version - just runs detection
    run_realtime_detection(MODEL_PATH, conf_threshold=0.25)
    
    # Interactive version with controls
    # run_with_options(MODEL_PATH)