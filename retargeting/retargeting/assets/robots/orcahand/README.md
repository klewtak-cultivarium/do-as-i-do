# OrcaHand v2 — Retargeting Pipeline Assets

Adapted OrcaHand v2 MJCF for the do-as-i-do retargeting pipeline. These files wrap the
official OrcaHand v2 kinematics (from [orcahand/orcahand_description](https://github.com/orcahand/orcahand_description))
in the pipeline's naming contract (6-DOF free base, fingertip/palm sites, collision capsules,
position actuators).

## Files

| File | Description |
|---|---|
| `right.xml` | Right-hand OrcaHand v2 (23 actuators: 6 base + 1 wrist + 16 finger) |
| `left.xml` | Left-hand OrcaHand v2 |
| `bimanual.xml` | Both hands in one model |
| `meshes/` | STL meshes (you must populate — see below) |

## Setup: fetch the meshes

The STL meshes are MIT-licensed from the OrcaHand team. Clone their description repo and copy
the v2 meshes:

```bash
cd retargeting/retargeting/assets/robots/orcahand

# Clone the official OrcaHand description repo
git clone https://github.com/orcahand/orcahand_description.git /tmp/orcahand_description

# Copy the v2 STL meshes
mkdir -p meshes/right meshes/left
cp /tmp/orcahand_description/v2/models/assets/right/*.stl meshes/right/
cp /tmp/orcahand_description/v2/models/assets/left/*.stl  meshes/left/
```

## OrcaHand v2 joint layout (17 hand DOF + 6 base)

| Joint | Range (rad) | Description |
|---|---|---|
| `{side}_wrist` | -1.134 to 0.611 | Hand wrist flexion |
| **Thumb** | | |
| `{side}_t-cmc` | -0.785 to 0.576 | Thumb CMC rotation |
| `{side}_t-abd` | -0.314 to 0.960 | Thumb abduction |
| `{side}_t-mcp` | -0.436 to 1.745 | Thumb MCP flexion |
| `{side}_t-pip` | -0.262 to 1.868 | Thumb PIP flexion |
| **Index/Middle/Ring/Pinky** (×4) | | |
| `{side}_{f}-abd` | ±0.47 to ±0.52 | Finger abduction |
| `{side}_{f}-mcp` | -0.436 to 1.745 | MCP flexion |
| `{side}_{f}-pip` | -0.262 to 1.868 | PIP flexion |

## Pipeline naming contract satisfied

- **Base joints:** `{side}_pos_x/y/z` (slide), `{side}_rot_x/y/z` (hinge) — first 6 qpos
- **Palm site:** `{side}_palm` (+ `collision_hand_{side}_palm_0`)
- **Fingertip sites:** `{side}_{finger}_tip`, `track_hand_{side}_{finger}_tip`, `trace_hand_{side}_{finger}_tip`
- **Collision capsules:** `collision_hand_{side}_{finger}_{0,1,2}[_3]`
- **Position actuators:** all joints (base kp=1000, hand kp=300)

## Usage

```bash
python launch.py --task <task> --raw-dir <reconstruction_output> --robot-type orcahand
```

## Notes

- **Fingertip site positions** (`pos="0 0 {offset}"` on each distal body) are initial estimates
  based on the OrcaHand body-tree dimensions. If IK convergence is poor, fine-tune the `TIP_Z`
  values in `gen_orcahand.py` by measuring the actual STL fingertip offset.
- **The `_UR3_FOREARM_DIRS` entry** for orcahand is `(0, 0, -1)` (tower extends in -Z from the
  palm). Adjust if the UR3e mount orientation differs.
- **Tendon coupling** (rolling-contact joints) is simplified to per-joint actuators — the real
  OrcaHand couples some joints via tendons. Hardware deployment uses `orca_core` which handles
  the tendon mapping.
