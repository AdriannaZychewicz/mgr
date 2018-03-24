from scipy import signal
import numpy as np

def process(self, wave):
    wave.check_mono()
    if wave.sample_rate != self.sr:
        raise Exception("Wrong sample rate")
    n = int(np.ceil(2 * wave.num_frames / float(self.w_len)))
    m = (n + 1) * self.w_len / 2
    swindow = self.make_signal_window(n)
    win_ratios = [self.window / swindow[t * self.w_len / 2:
                                        t * self.w_len / 2 + self.w_len]
                  for t in range(n)]
    wave = wave.zero_pad(0, int(m - wave.num_frames))
    wave = audio.Wave(signal.hilbert(wave), wave.sample_rate)
    result = np.zeros((self.n_bins, n))

    for b in range(self.n_bins):
        w = self.widths[b]
        wc = 1 / np.square(w + 1)
        filter = self.filters[b]
        band = fftfilt(filter, wave.zero_pad(0, int(2 * w))[:, 0])
        band = band[int(w): int(w + m), np.newaxis]
        for t in range(n):
            frame = band[t * self.w_len / 2:
                         t * self.w_len / 2 + self.w_len, :] * win_ratios[t]
            result[b, t] = wc * np.real(np.conj(np.dot(frame.conj().T, frame)))
    return audio.Spectrogram(result, self.sr, self.w_len, self.w_len / 2)