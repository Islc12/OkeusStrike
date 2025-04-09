# OkeusStrike - Advanced Deauthentication Attack Tool - input.py
# Copyright (C) 2025 Richard Smith (Islc12)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import struct

def reasoncode_input(reason):
    reasoncode = {
    0: struct.pack('H', 0x00), # No reason code
    1: struct.pack('<H', 0x01), # - Code 1: Unspecified reason. - \x00\x01
    2: struct.pack('<H', 0x02), # - Code 2: Previous authentication is no longer valid. - \x00\x02
    3: struct.pack('<H', 0x03), # - Code 3: Station has left the Basic Service Set (BSS) or Extended Service Set (ESS). - \x00\x03
    4: struct.pack('<H', 0x04), # - Code 4: Inactivity timer expired. - \x00\x04
    5: struct.pack('<H', 0x05), # - Code 5: Disassociated due to insufficient resources at the AP. - \x00\x05
    6: struct.pack('<H', 0x06), # - Code 6: Class 2 frame received from a nonauthenticated station. - \x00\x06
    7: struct.pack('<H', 0x07), # - Code 7: Class 3 frame received from a nonassociated station. - \x00\x07
    8: struct.pack('<H', 0x08), # - Code 8: Station has left the BSS or ESS (disassociation). - \x00\x08
    9: struct.pack('<H', 0x09), # - Code 9: Station is attempted to authenticate with an AP that doesn't support the authentication protocol. - \x00\x09
    10: struct.pack('<H', 0x0A), # - Code 10: Specified timeout - \x00\x0A
    11: struct.pack('<H', 0x0B), # - Code 11: Group Key Update Timeout - \x00\x0B
    12: struct.pack('<H', 0x0C), # - Code 12: Unspecified reason (disassociation). - \x00\x0C
    13: struct.pack('<H', 0x0D), # - Code 13: Invalid information - \x00\x0D
    14: struct.pack('<H', 0x0E), # - Code 14: Incompatible parameters - \x00\x0E
    15: struct.pack('<H', 0x0F),
    16: struct.pack('<H', 0x10),
    17: struct.pack('<H', 0x11),
    18: struct.pack('<H', 0x12),
    19: struct.pack('<H', 0x13),
    20: struct.pack('<H', 0x14),
    21: struct.pack('<H', 0x15),
    22: struct.pack('<H', 0x16),
    23: struct.pack('<H', 0x17),
    24: struct.pack('<H', 0x18),
    25: struct.pack('<H', 0x19),
    26: struct.pack('<H', 0x1A),
    27: struct.pack('<H', 0x1B),
    28: struct.pack('<H', 0x1C),
    29: struct.pack('<H', 0x1D),
    30: struct.pack('<H', 0x1E),
    31: struct.pack('<H', 0x1F),
    32: struct.pack('<H', 0x20),
    33: struct.pack('<H', 0x21),
    34: struct.pack('<H', 0x22),
    35: struct.pack('<H', 0x23),
    36: struct.pack('<H', 0x24),
    37: struct.pack('<H', 0x25),
    38: struct.pack('<H', 0x26),
    39: struct.pack('<H', 0x27),
    40: struct.pack('<H', 0x28),
    41: struct.pack('<H', 0x29),
    42: struct.pack('<H', 0x2A),
    43: struct.pack('<H', 0x2B),
    44: struct.pack('<H', 0x2C),
    45: struct.pack('<H', 0x2D),
    46: struct.pack('<H', 0x2E),
    47: struct.pack('<H', 0x2F),
    48: struct.pack('<H', 0x30),
    49: struct.pack('<H', 0x31),
    50: struct.pack('<H', 0x32),
    51: struct.pack('<H', 0x33),
    52: struct.pack('<H', 0x34),
    53: struct.pack('<H', 0x35),
    54: struct.pack('<H', 0x36),
    55: struct.pack('<H', 0x37),
    56: struct.pack('<H', 0x38),
    57: struct.pack('<H', 0x39),
    58: struct.pack('<H', 0x3A),
    59: struct.pack('<H', 0x3B),
    60: struct.pack('<H', 0x3C),
    61: struct.pack('<H', 0x3D),
    62: struct.pack('<H', 0x3E),
    63: struct.pack('<H', 0x3F),
    64: struct.pack('<H', 0x40),
    65: struct.pack('<H', 0x41),
    66: struct.pack('<H', 0x42)
    }

    rc = reasoncode.get(reason)
    return rc

def def_code(reason):
    code_def = {
        0: "No reason code assigned **** MALFORMED PACKET ERROR ****",
        1: "Unspecified reason",
        2: "Previous authentication no longer valid",
        3: "Deauthenticated because sending STA is leaving (or has left) IBSS or ESS",
        4: "Disassociated due to inactivity",
        5: "Disassociated because AP is unable to handle all currently associated STAs",
        6: "Class 2 frame received from nonauthenticated STA",
        7: "Class 3 frame received from nonassociated STA",
        8: "Disassociated because sending STA is leaving (or has left) BSS",
        9: "STA requesting (re)association is not authenticated with responding STA.",
        10: "Disassociated because the information in the Power Capability element is unacceptable",
        11: "Disassociated because the information in the Supported Channels element is unacceptable",
        12: "Disassociated due to BSS Transition Management",
        13: "Invalid element, that is, an element defined in this standard for which the content does not meet the specifications in Clause 8.",
        14: "Message integrity code (MIC) failure",
        15: "4-Way Handshake timeout",
        16: "Group Key Handshake timeout",
        17: "Element in 4-Way Handshake is different from (Re)Association Request/Probe Response/Beacon frame.",
        18: "Invalid group cipher",
        19: "Invalid pairwise cipher",
        20: "Invalid AKMP",
        21: "Unsupported RSNE version",
        22: "Invalid RSNE capabilities",
        23: "IEEE 802.1X authentication failed.",
        24: "Cipher suite rejected because of the security policy.",
        25: "TDLS direct-link teardown because TDLS peer STA is unreachable via the TDLS direct link.",
        26: "TDLS direct-link teardown for unspecified reason.",
        27: "Disassociated because the session is terminated by SSP request.",
        28: "Disassociated because of the lack of SSP roaming agreement.",
        29: "Requested service rejected because of SSP cipher suite or AKM requirement.",
        30: "Requested service not authorized in this location.",
        31: "TS was deleted because QoS AP lacks sufficient bandwidth for this QoS STA due to a change in BSS service characteristics or operational mode (example: an HT BSS change from 40 MHz channel to 20 MHz channel).",
        32: "Disassociated for unspecified, QoS-related reason.",
        33: "Disassociated because QoS AP lacks sufficient bandwidth for this QoS STA.",
        34: "Disassociated because excessive number of frames need to be acknowledged, but are not acknowledged because of AP transmissions or poor channel conditions.",
        35: "Disassociated because STA is transmitting outside the limits of its TXOPs.",
        36: "STA_LEAVING requested from peer STA as the STA is leaving the BSS (or resetting).",
        37: "Requested from peer STA as it does not want to use the mechanism.",
        38: "Requested from peer STA as the STA received frames using the mechanism for which a setup is required.",
        39: "Requested from peer STA due to timeout.",
        40: "N",
        41: "N",
        42: "N",
        43: "N",
        44: "N",
        45: "Peer STA does not support the requested cipher suite.",
        46: "In a DLS teardown frame: The teardown was initiated by the DLS peer. In a Disassociation frame: Disassociated because authorized access limit reached.",
        47: "In a DLS teardown frame: The teardown was initiated by the AP. In a Disassociation frame: Disassociated due to external service requirements.",
        48: "Invalid FT Action frame count",
        49: "Invalid pairwise master key identifier (PMKI)",
        50: "Invalid MDE",
        51: "Invalid FTE",
        52: "SME cancels the mesh peering instance with the reason other than reaching the maximum number of peer mesh STAs.",
        53: "The mesh STA has reached the supported maximum number of peer mesh STAs.",
        54: "The received information violates the Mesh Configuration policy configured in the mesh STA profile.",
        55: "The mesh STA has received a Mesh Peering Close message requesting to close the mesh peering.",
        56: "The mesh STA has resent dot11MeshMaxRetries Mesh Peering Open messages, without receiving a Mesh Peering Confirm message.",
        57: "The confirmTimer for the mesh peering instance times out.",
        58: "The mesh STA fails to unwrap the GTK or the values in the wrapped contents do not match.",
        59: "The mesh STA receives inconsistent information about the mesh parameters between Mesh Peering Management frames.",
        60: "The mesh STA fails the authenticated mesh peering exchange because of a failure in selecting either the pairwise ciphersuite or group ciphersuite.",
        61: "The mesh STA does not have proxy information for this external destination.",
        62: "The mesh STA does not have forwarding information for this destination.",
        63: "The mesh STA determines that the link to the next hop of an active path in its forwarding information is no longer usable.",
        64: "The deauthentication frame was sent because the MAC address of the STA already exists in the mesh BSS. See 10.3.6.",
        65: "The mesh STA performs channel switch to meet regulatory requirements.",
        66: "The mesh STA performs channel switch with unspecified reason."
        }

    cd = code_def.get(reason)
    return cd