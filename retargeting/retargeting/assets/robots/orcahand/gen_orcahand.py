#!/usr/bin/env python3
"""Generate pipeline-compatible OrcaHand v2 MJCF (right.xml + left.xml).

Wraps the official OrcaHand v2 body tree in the do-as-i-do retargeting naming contract.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))  # orcahand/ directory

# ─── OrcaHand v2 kinematic chain (transcribed EXACTLY from orcahand_description/v2) ───
# Each finger: list of (suffix, pos, quat, joint_name, joint_axis, joint_range, mesh_or_None)
# Bodies nest sequentially (each inside the previous); the first nests inside carpals.

FINGERS = {
    "thumb": [
        ("cmc", [-0.021213412275949937, 0.01433246945435063, -0.02172481544690429],
         [0.6591193783565908, 0.35951060036119065, -0.07247312029417424, -0.656552678874735],
         "t-cmc", [-7.77e-16, 5.41e-16, -1.0], [-0.7853981633974483, 0.5759586531581288], "T-TP-R"),
        ("ap", [-0.036, 1.39e-17, -7.63e-17],
         [0.819152044288991, -0.5735764363510464, -2.22e-16, -1.55e-15],
         "t-abd", [-1.50e-15, 0.3420201433256641, 0.9396926207859044], [-0.3141592653589793, 0.9599310885968813], "R-T-AP"),
        ("pp", [5.03e-17, 1.02e-17, 2.91e-17],
         [1.22e-15, 0.7071067811865461, -1.39e-15, -0.7071067811865444],
         "t-mcp", [-3.14e-15, -1.0, 2.94e-15], [-0.4363323129985824, 1.7453292519943295], "T-PP"),
        ("dp", [0.001, 5.20e-18, 0.032],
         [1.0, 0.0, -2.78e-17, -1.92e-15],
         "t-pip", [4.72e-16, -1.0, 3.16e-15], [-0.2617993877991494, 1.8675022996339325], None),
    ],
    "index": [
        ("ap", [-0.025575481691250117, 0.0006809253025602396, 0.03835732632869239],
         [0.519646788331587, 0.5667240334680995, 0.4317303415794619, -0.4715930421730138],
         "i-abd", [-8.33e-17, 3.33e-16, 1.0], [-0.4363323129985824, 0.5235987755982988], "I-AP-R"),
        ("pp", [-0.0004009681508766414, -1.76e-17, 2.89e-15],
         [0.7071067811865461, 1.85e-15, -0.7071067811865465, -2.05e-15],
         "i-mcp", [5.83e-15, -1.0, 1.11e-16], [-0.4363323129985824, 1.7453292519943295], "I-PP"),
        ("tip", [0.0015, 8.67e-18, 0.037],
         [1.0, 1.67e-16, 4.16e-17, 3.39e-15],
         "i-pip", [-3.61e-15, -1.0, 2.78e-16], [-0.2617993877991494, 1.8675022996339325], None),
    ],
    "middle": [
        ("ap", [-0.0007567300518294843, -0.0011463260089169605, 0.04825182678794436],
         [-0.5006540699144025, -0.5006540699144022, -0.4993450733492283, 0.4993450733492286],
         "m-abd", [1.11e-15, -2.22e-16, 1.0], [-0.47123889803846897, 0.47123889803846897], "M-AP"),
        ("pp", [-0.000616967942905312, -1.84e-17, 4.37e-15],
         [-0.7071067811865464, -2.22e-15, 0.7071067811865461, 2.22e-15],
         "m-mcp", [6.05e-15, -1.0, -1.11e-16], [-0.4363323129985824, 1.7453292519943295], "M-PP"),
        ("tip", [0.002, -3.47e-18, 0.040],
         [1.0, 2.78e-16, 1.39e-16, 3.28e-15],
         "m-pip", [-3.28e-15, -1.0, 4.44e-16], [-0.2617993877991494, 1.8675022996339325], None),
    ],
    "ring": [
        ("ap", [0.02300540741341827, -0.0001014498859375039, 0.04085073553625944],
         [-0.4851713041498216, -0.43849204432323763, -0.554729417883375, 0.514401405159008],
         "r-abd", [8.88e-16, -5.55e-17, 1.0], [-0.47123889803846897, 0.47123889803846897], "M-AP"),
        ("pp", [-0.0006169679429055062, 2.99e-17, 4.53e-15],
         [-0.7071067811865464, -2.10e-15, 0.7071067811865462, 2.0e-15],
         "r-mcp", [5.94e-15, -1.0, 1.11e-16], [-0.4363323129985824, 1.7453292519943295], "M-PP"),
        ("tip", [0.002, -6.94e-18, 0.040],
         [1.0, 1.11e-16, 5.55e-17, 3.11e-15],
         "r-pip", [-2.94e-15, -1.0, 2.22e-16], [-0.2617993877991494, 1.8675022996339325], None),
    ],
    "pinky": [
        ("ap", [0.04666877715017955, 0.00500098395792942, 0.029101417458615046],
         [-0.45731846125607556, -0.3401988014151619, -0.6138690651598068, 0.5461587418964287],
         "p-abd", [9.71e-16, 1.67e-16, 1.0], [-0.5235987755982988, 0.5235987755982988], "P-AP"),
        ("pp", [-7.08e-17, -3.18e-17, -1.36e-17],
         [-0.7071067811865464, -2.0e-15, 0.707106781186546, 2.11e-15],
         "p-mcp", [6.44e-15, -1.0, 6.66e-16], [-0.4363323129985824, 1.7453292519943295], "P-PP"),
        ("tip", [0.001, 3.12e-17, 0.031],
         [1.0, 5.55e-17, 1.39e-17, 3.11e-15],
         "p-pip", [-2.61e-15, -1.0, 3.89e-16], [-0.2617993877991494, 1.8675022996339325], None),
    ],
}

# Structural chain: palm → forearm → toptower → carpals (fingers branch from carpals)
STRUCT = [
    ("forearm", [0, 0, 0], [1, 0, 0, 0], None, None, None, "ForeArmStructure-Model"),
    ("toptower", [-0.010000000000000018, 0.05230000000000584, -2.08e-17],
     [-0.4999999999999985, 0.4999999999999986, -0.5, -0.49999999999999994],
     None, None, None, "TopTower-Model"),
    ("carpals", [-0.0018770780631086163, 0.005000000000000039, 0.08950000067055244],
     [-0.7071067811865475, 0.0, 0.0, 0.7071067811865495],
     "wrist", [-1.0, -1.13e-16, 5.94e-17], [-1.1344640137963142, 0.6108652381980153], "R-Carpals"),
]

# Mesh files (shared between right/left, just the prefix dir differs)
MESH_FILES = {
    "ForeArmStructure-Model": "ForeArmStructure-Model.stl",
    "ForeArmStructure-Model_Logo": "ForeArmStructure-Model_Logo.stl",
    "TopTower-Model": "TopTower-Model.stl",
    "R-Carpals": "R-Carpals.stl", "L-Carpals": "L-Carpals.stl",
    "T-TP-R": "T-TP-R.stl", "T-TP-L": "T-TP-L.stl",
    "R-T-AP": "R-T-AP.stl", "L-T-AP": "L-T-AP.stl",
    "T-PP": "T-PP.stl", "T-PP_Skin": "T-PP_Skin.stl", "T-PP_PP": "T-PP_PP.stl",
    "T-DP_Skin": "T-DP_Skin.stl", "T-DP_T-DP": "T-DP_T-DP.stl",
    "I-AP-R": "I-AP-R.stl", "I-AP-L": "I-AP-L.stl",
    "I-PP": "I-PP.stl", "I-PP_Skin": "I-PP_Skin.stl", "I-PP_PP": "I-PP_PP.stl",
    "I-IP_IP": "I-IP_IP.stl", "I-FingerTipAssembly_I-DP-Skin": "I-FingerTipAssembly_I-DP-Skin.stl",
    "M-AP": "M-AP.stl", "M-PP": "M-PP.stl", "M-PP_Skin": "M-PP_Skin.stl", "M-PP_PP": "M-PP_PP.stl",
    "M-IP_IP": "M-IP_IP.stl", "M-FingerTipAssembly_M-DP-Skin": "M-FingerTipAssembly_M-DP-Skin.stl",
    "P-AP": "P-AP.stl", "P-PP": "P-PP.stl", "P-PP_Skin": "P-PP_Skin.stl", "P-PP_PP": "P-PP_PP.stl",
    "P-IP_IP": "P-IP_IP.stl", "P-FingerTipAssembly_P-DP-Skin": "P-FingerTipAssembly_P-DP-Skin.stl",
}

TIP_Z = {"thumb": 0.015, "index": 0.015, "middle": 0.015, "ring": 0.015, "pinky": 0.012}
CAP_R = {"thumb": [0.007, 0.010, 0.012, 0.012],
         "index": [0.007, 0.009, 0.010], "middle": [0.007, 0.009, 0.010],
         "ring": [0.007, 0.009, 0.010], "pinky": [0.006, 0.008, 0.009]}
CAP_L = {"thumb": [0.020, 0.030, 0.028, 0.020],
         "index": [0.022, 0.037, 0.025], "middle": [0.022, 0.040, 0.025],
         "ring": [0.022, 0.040, 0.025], "pinky": [0.020, 0.031, 0.023]}


def F(arr):
    return " ".join(f"{float(x):.16g}" for x in arr)

def R(arr):
    return " ".join(f"{float(x):.8g}" for x in arr)


def gen(side):
    L = []  # output lines
    a = lambda s: L.append(s)
    s = side
    P = side == "right"

    a(f'<mujoco model="orcahand_{s}">')
    a(f'  <compiler angle="radian" meshdir="meshes/" autolimits="true" />')
    a(f'  <default>')
    a(f'    <geom density="800" condim="1" contype="0" conaffinity="0" />')
    a(f'    <position kp="300" dampratio="1.0" inheritrange="1" />')
    a(f'    <joint damping="0.0" armature="1.0" frictionloss="0.0" />')
    a(f'    <site size="0.005" type="sphere" rgba="1 0 0 1" group="3" />')
    a(f'  </default>')
    a(f'  <asset>')

    # Pick correct L/R mesh variant for side-specific parts
    def mesh_name(base):
        if base in ("T-TP-R", "T-TP-L"): return base if P else base.replace("-R", "-L")
        if base in ("I-AP-R", "I-AP-L"): return base if P else base.replace("-R", "-L")
        if base == "R-Carpals": return "R-Carpals" if P else "L-Carpals"
        if base == "R-T-AP": return "R-T-AP" if P else "L-T-AP"
        return base

    # Opposite-side-only mesh variants that don't exist in this side's mesh dir
    skip = {"T-TP-L", "I-AP-L", "L-Carpals", "L-T-AP"} if P else {"T-TP-R", "I-AP-R", "R-Carpals", "R-T-AP"}
    for name, file in sorted(MESH_FILES.items()):
        if name in skip:
            continue
        a(f'    <mesh name="{s}_{name}" file="{s}/{file}" />')
    a(f'  </asset>')

    # ─── Worldbody ───
    a(f'  <worldbody>')

    # 6-DOF free base (identical to sharpa)
    base_defs = [
        ("base_tx", "pos_x", "1 0 0", "slide", "-5 5"),
        ("base_ty", "pos_y", "0 1 0", "slide", "-5 5"),
        ("base_tz", "pos_z", "0 0 1", "slide", "-5 5"),
        ("base_roll", "rot_x", "1 0 0", "hinge", "-6.28 6.28"),
        ("base_pitch", "rot_y", "0 1 0", "hinge", "-6.28 6.28"),
        ("base_yaw", "rot_z", "0 0 1", "hinge", "-6.28 6.28"),
    ]
    depth = 2  # inside worldbody
    for bname, jname, axis, jtype, jrange in base_defs:
        ind = "  " * depth
        a(f'{ind}<body name="{s}_{bname}">')
        a(f'{ind}  <inertial pos="0 0 0" mass="0.1" diaginertia="0.01 0.01 0.01" />')
        a(f'{ind}  <joint name="{s}_{jname}" pos="0 0 0" axis="{axis}" type="{jtype}" range="{jrange}" />')
        depth += 1

    # Palm root body
    ind = "  " * depth
    a(f'{ind}<body name="{s}_hand_palm" pos="0 0 0">')
    a(f'{ind}  <inertial pos="0.006 0.001 0.039" mass="0.72" diaginertia="0.000713 0.000814 0.000208" />')
    a(f'{ind}  <geom type="mesh" contype="0" conaffinity="0" group="1" density="0" rgba="0.79 0.82 0.93 1" '
      f'mesh="{s}_ForeArmStructure-Model" name="{s}_hand_palm_visual" />')
    a(f'{ind}  <geom name="collision_hand_{s}_palm_0" type="box" '
      f'size="0.016 0.035 0.035" pos="0 0 0.05" group="3" rgba="0 1 0 1" />')
    a(f'{ind}  <site name="{s}_palm" pos="0 0 0.05" type="box" size="0.01 0.02 0.03" />')
    depth += 1

    # Structural chain: forearm → toptower → carpals
    for (short, pos, quat, jname, jaxis, jrange, mesh) in STRUCT:
        ind = "  " * depth
        mn = mesh_name(mesh)
        a(f'{ind}<body name="{s}_{short}" pos="{F(pos)}" quat="{F(quat)}">')
        if jname:
            a(f'{ind}  <inertial pos="0 0 0" mass="0.1" diaginertia="1e-4 1e-4 1e-4" />')
            a(f'{ind}  <joint name="{s}_{jname}" pos="0 0 0" axis="{F(jaxis)}" range="{R(jrange)}" ref="0.0" />')
        a(f'{ind}  <geom type="mesh" contype="0" conaffinity="0" group="1" density="0" '
          f'rgba="0.79 0.82 0.93 1" mesh="{s}_{mn}" />')
        depth += 1

    # Fingers — branch from carpals
    for fname, segs in FINGERS.items():
        n = len(segs)
        for i, (suffix, pos, quat, jname, jaxis, jrange, mesh) in enumerate(segs):
            ind = "  " * depth
            bname = f"{s}_{fname}_{suffix}"
            a(f'{ind}<body name="{bname}" pos="{F(pos)}" quat="{F(quat)}">')
            ci = "  " * (depth + 1)
            if jname:
                a(f'{ci}<inertial pos="0 0 0" mass="0.01" diaginertia="1e-6 1e-6 1e-6" />')
                a(f'{ci}<joint name="{s}_{jname}" pos="0 0 0" axis="{F(jaxis)}" range="{R(jrange)}" ref="0.0" />')
            if mesh:
                mn = mesh_name(mesh)
                a(f'{ci}<geom type="mesh" contype="0" conaffinity="0" group="1" density="0" '
                  f'rgba="0.79 0.82 0.93 1" mesh="{s}_{mn}" />')
            # Collision capsule: _0 at tip, _1 one-back, _2 two-back, _3 three-back
            cap_n = n - 1 - i
            if cap_n <= 3:
                r = CAP_R[fname][cap_n] if cap_n < len(CAP_R[fname]) else CAP_R[fname][-1]
                l = CAP_L[fname][cap_n] if cap_n < len(CAP_L[fname]) else CAP_L[fname][-1]
                a(f'{ci}<geom name="collision_hand_{s}_{fname}_{cap_n}" type="capsule" '
                  f'size="{r:.4f}" fromto="0 0 {l:.4f} 0 0 0" group="3" rgba="0 1 0 1" />')
            # Fingertip sites on last body
            if i == n - 1:
                tz = TIP_Z[fname]
                a(f'{ci}<site name="{s}_{fname}_tip" pos="0 0 {tz:.4f}" />')
                a(f'{ci}<site name="track_hand_{s}_{fname}_tip" pos="0 0 {tz:.4f}" />')
                a(f'{ci}<site name="trace_hand_{s}_{fname}_tip" pos="0 0 {tz:.4f}" />')
            depth += 1
        # Close finger bodies
        for _ in range(n):
            depth -= 1
            a(f'{"  " * depth}</body>')

    # Close structural chain
    for _ in STRUCT:
        depth -= 1
        a(f'{"  " * depth}</body>')
    # Close palm
    depth -= 1
    a(f'{"  " * depth}</body>')
    # Close base
    for _ in base_defs:
        depth -= 1
        a(f'{"  " * depth}</body>')
    a(f'  </worldbody>')

    # ─── Actuators ───
    a(f'  <actuator>')
    for jname in ["pos_x", "pos_y", "pos_z", "rot_x", "rot_y", "rot_z"]:
        a(f'    <position name="{s}_{jname}_position" joint="{s}_{jname}" kp="1000" />')
    a(f'    <position name="{s}_wrist_position" joint="{s}_wrist" />')
    for fname in ["thumb", "index", "middle", "ring", "pinky"]:
        for seg in FINGERS[fname]:
            jn = seg[3]  # joint_name
            a(f'    <position name="{s}_{jn}_position" joint="{s}_{jn}" />')
    a(f'  </actuator>')
    a(f'</mujoco>')
    return "\n".join(L) + "\n"


for side in ("right", "left"):
    xml = gen(side)
    path = os.path.join(OUT, f"{side}.xml")
    with open(path, "w") as f:
        f.write(xml)
    print(f"Wrote {path} ({len(xml)} bytes, {xml.count(chr(10))} lines)")
