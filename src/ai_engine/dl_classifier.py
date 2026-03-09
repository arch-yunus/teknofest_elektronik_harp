import numpy as np
import logging

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    logging.warning("PyTorch not installed. DL features disabled.")

if TORCH_AVAILABLE:
    class ConvNetIQ(nn.Module):
        """
        A standard Convolutional Neural Network for processing 1D raw I/Q sequences
        or spectral magnitudes to classify Electronic Warfare signals.
        """
        def __init__(self, num_classes=7):
            super(ConvNetIQ, self).__init__()
            # Assuming input shape: (batch_size, 1, sequence_length)
            # In practice, I/Q can be 2 channels: (batch_size, 2, sequence_length)
            # For simplicity, we use 1 channel (e.g., magnitude spectrum or flattened I/Q)
            self.conv1 = nn.Conv1d(in_channels=1, out_channels=16, kernel_size=7, stride=2, padding=3)
            self.pool1 = nn.MaxPool1d(kernel_size=2, stride=2)
            self.conv2 = nn.Conv1d(in_channels=16, out_channels=32, kernel_size=5, stride=2, padding=2)
            self.pool2 = nn.MaxPool1d(kernel_size=2, stride=2)
            self.conv3 = nn.Conv1d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
            
            # Using AdaptiveAvgPool1d to make the model invariant to input sequence length
            self.adaptive_pool = nn.AdaptiveAvgPool1d(1)
            
            self.fc1 = nn.Linear(64, 32)
            self.fc2 = nn.Linear(32, num_classes)
            
        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = self.pool1(x)
            x = F.relu(self.conv2(x))
            x = self.pool2(x)
            x = F.relu(self.conv3(x))
            
            x = self.adaptive_pool(x)
            # Flatten
            x = x.view(x.size(0), -1)
            
            x = F.relu(self.fc1(x))
            x = self.fc2(x)
            return x

class DummyDLClassifier:
    """
    Wrapper for the DL model supporting inference and dummy weights initialization.
    Designed to gracefully fail if PyTorch is not available.
    """
    def __init__(self):
        self.labels = ["Noise", "CW", "BPSK", "QPSK", "Pulsed_Radar", "FHSS", "LPI_Radar"]
        self.model = None
        self.device = None
        
        if TORCH_AVAILABLE:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.model = ConvNetIQ(num_classes=len(self.labels)).to(self.device)
            self.model.eval()  # Set to evaluation mode
            logging.info(f"Initialized PyTorch DL model on {self.device}")
        
    def predict_from_magnitudes(self, magnitudes):
        """
        Runs inference on given magnitudes (fft output).
        Returns classification label and confidence.
        """
        if not TORCH_AVAILABLE or self.model is None:
            return None, 0.0
            
        try:
            # Reshape magnitude array to (batch_size, channels, sequence_length)
            # e.g., (1, 1, 1024)
            data_tensor = torch.tensor(magnitudes, dtype=torch.float32).unsqueeze(0).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                logits = self.model(data_tensor)
                probs = F.softmax(logits, dim=1)
                
                # Get max probability and corresponding index
                max_prob, predicted_class = torch.max(probs, 1)
                
                confidence = max_prob.item()
                label_idx = predicted_class.item()
                
            # If the weights are entirely random, it's just producing noise predictions.
            # Real deployment would load a .pt file here.
            return self.labels[label_idx], confidence
            
        except Exception as e:
            logging.error(f"DL Inference error: {e}")
            return None, 0.0
