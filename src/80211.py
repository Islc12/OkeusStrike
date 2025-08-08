import struct
import sys
import random

class Dot11Frame:
    def __init__(self, frag=None, randfrag=False, dur=None, dest_mac=None,
                    broadcast_attack=False, source_mac=None, network_bssid=None,
                    autoseq=False, seq_num=False, reason_code=None, body_bytes=None):
        self.frag = frag
        self.randfrag = randfrag
        self.dur = dur
        self.dest_mac = dest_mac
        self.broadcast_attack = broadcast_attack
        self.source_mac = source_mac
        self.network_bssid = network_bssid
        self.autoseq = autoseq
        self.seq_num = seq_num
        self.reason_code = reason_code
        self.body_bytes = bodybytes

    def manage_field(self):
        f_ctl = struct.pack('B', 0xC0)

    def frame_ctrl_field(self):
        # FCF
        match (self.frag, self.randfrag):
            case (None, False):
                self.f_frag = struct.pack('B', 0x00)
            case (_, False):
                self.f_frag = struct.pack('B', 0x20)
                self.ver_fcf = "MANUAL"
            case (None, True):
                self.f_frag = struct.pack('B', 0x20)
                self.ver_fcf = "RANDOM"

    def duration_field(self):
        if self.dur is None:
            self.f_dur = struct.pack('<H', 0x00)
        else:
            self.f_dur = struct.pack('<H', self.dur & 0xFFFF)

    def addr1_field(self):
        match (self.dest_mac, self.broadcast_attack):
            case (None, False):
                print("Invalid input, need address 1 field")
                sys.exit(exit.EXIT_NO_TARGET)
            case (None, True):
                self.addr1 = struct.pack('!6B', 0xFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF)
            case (_, False):
                self.addr1 = convert.machex(self.dest_mac)
            case (_, True):
                print("Invalid arguments, too many addresses in Address 1")
                sys.exit(exit.EXIT_TOO_MANY_ADDR1)

    def addr2_field(self):
        if self.source_mac is None:
            self.addr2 = convert.machex(self.network_bssid)
            print("Source Address (Address 2) field will use Network Address (Address 3 field)")
        else:
            self.addr2 = convert.machex(self.source_mac)

    def addr3_field(self):
        if self.network_bssid is None:
            print("Invalid argument, missing Address 3")
            sys.exit(exit.EXIT_NO_NETWORKBSSID)
        else:
            self.addr3 = convert.machex(self.network_bssid)

### this is literally just copy and paste from other files, we'll actually do something with it in a little bit. For now, sleep...


    def seq_control_field(self):
        # upgrade this to a match case statement to clean it up
        
        if not hasattr(fs, "sn"):
            fs.sn = 1
        if all(x is None for x in (frag, seq_num)) and not (randfrag or autoseq):
            seq = struct.pack('<H', 0x00)

        if randfrag and not (frag or seq_num or autoseq):
            rf = random.randint(1, 14)
            seq = struct.pack('<H', rf & 0x0F)
        elif autoseq and not (frag or seq_num or randfrag):
            seq = struct.pack('<H', (fs.sn << 4) & 0xFFF0)
            fs.sn += 1
        elif (autoseq and randfrag) and not (seq_num or frag):
            rf = random.randint(1, 14)
            if rf >= 8:
                seq = struct.pack('<H', ((fs.sn << 4) & 0xFFF0) | (rf & 0x0F))
                fs.sn += 1
            else:
                seq = struct.pack('<H', (fs.sn << 4) & 0xFFF0)
        elif (randfrag and seq_num) and not (frag or autoseq):
            rf = random.randint(1, 14)
            seq = struct.pack('<H', ((seq_num << 4) & 0xFFF0) | (rf & 0x0F))
        elif frag and not (seq_num or randfrag or autoseq):
            seq = struct.pack('<H', frag & 0x0F)
        elif (frag and autoseq) and not (randfrag or seq_num):
            seq = struct.pack('<H', ((fs.sn << 4) & 0xFFF0) | (frag & 0x0F))
            fs.sn += 1
        elif (frag and seq_num) and not (randfrag or autoseq):
            seq = struct.pack('<H', ((seq_num << 4) & 0xFFF0) | (frag & 0x0F))
        elif (seq_num) and not (frag or randfrag or autoseq):
            seq = struct.pack('<H', ((seq_num << 4) & 0xFFF0) )

    def reasoncode_field(self):
        match reason:
            case None:
                reasoncode_input(0)
            case _:
                reasoncode_input(reason)

    def body_field(self):
        match num:
            case None:
                return None
            case _:
                padding = struct.pack(f'{num}x')

        # Return the assembled parts (or just store them internally if desired)
        return self.f_ctl, self.f_frag, self.f_dur, self.addr1, self.addr2, self.addr3, self.ver_fcf