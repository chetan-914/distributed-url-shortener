import time
import threading

class SnowflakeIDGenerator:
    def __init__(self, machine_id, epoch=1704067200000):
        """
        :param machine_id: Unique ID for this instance (0-1023)
        :param epoch: Custom start timestamp in milliseconds
        """
        # Configuration: 41 (time) + 10 (machine) + 12 (sequence) = 63 bits (+1 sign bit)
        self.machine_id_bits = 10
        self.sequence_bits = 12
        
        # Max values for validation
        self.max_machine_id = -1 ^ (-1 << self.machine_id_bits)
        self.sequence_mask = -1 ^ (-1 << self.sequence_bits)
        
        if machine_id > self.max_machine_id or machine_id < 0:
            raise ValueError(f"Machine ID must be between 0 and {self.max_machine_id}")

        # Internal State
        self.machine_id = machine_id
        self.epoch = epoch
        self.last_timestamp = -1
        self.sequence = 0
        
        # Thread safety
        self.lock = threading.Lock()

    def _current_ms(self):
        return int(time.time() * 1000)

    def generate_id(self):
        with self.lock:
            current_timestamp = self._current_ms()

            # 1. Handle Clock Drift (Backwards)
            if current_timestamp < self.last_timestamp:
                drift = self.last_timestamp - current_timestamp
                raise RuntimeError(f"Clock moved backwards! Rejecting for {drift}ms")

            # 2. Sequence Logic
            if current_timestamp == self.last_timestamp:
                # Same millisecond: increment sequence and mask to 12 bits
                self.sequence = (self.sequence + 1) & self.sequence_mask
                if self.sequence == 0:
                    # Sequence overflow: wait for next millisecond
                    while current_timestamp <= self.last_timestamp:
                        current_timestamp = self._current_ms()
            else:
                # New millisecond: reset sequence
                self.sequence = 0

            self.last_timestamp = current_timestamp

            # 3. Bit Shifting
            # Shift timestamp 22 bits (10 machine + 12 sequence)
            # Shift machine_id 12 bits (sequence)
            id_val = ((current_timestamp - self.epoch) << (self.machine_id_bits + self.sequence_bits)) | \
                     (self.machine_id << self.sequence_bits) | \
                     self.sequence
            
            return id_val
        
generator = SnowflakeIDGenerator(machine_id=1)