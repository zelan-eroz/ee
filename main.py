import numpy as np
def calculate_snr(contaminated_signal, clean_eeg, artifact_segment):
    # Calculate the signal power (clean EEG)
    signal_power = np.sum(clean_eeg ** 2)
    # Calculate the noise power (artifact segment)
    noise_power = np.sum((contaminated_signal - clean_eeg) ** 2)
    # Calculate the SNR in dB (RMS FORMULA)
    snr_db = 10 * np.log10(signal_power / noise_power)
    return snr_db

# Example usage:
clean_eeg = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
artifact_segment = np.array([0.1, 0.2, 0.3, 0.2, 0.1])
λ = 0.5

contaminated_signal = clean_eeg + λ * artifact_segment
snr = calculate_snr(contaminated_signal, clean_eeg, artifact_segment)
print("SNR:", snr)