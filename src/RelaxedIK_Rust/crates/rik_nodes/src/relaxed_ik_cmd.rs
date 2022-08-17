use std::env;
use librelaxed_ik::utils_rust::subscriber_utils::EEPoseGoalsSubscriber;
use nalgebra::{Vector3, UnitQuaternion, Quaternion};


fn main() {
    // Expects:          --- seed state --       position   quaternion
    //     bin_name     "[j1, j2, ..., jn]"    "[x, y, z,   x, y, z, w]"   "info_file_path"
    let args: Vec<String> = env::args().collect();

    // Create the EEPoseGoal
    let mut g = EEPoseGoalsSubscriber::new();
    g.seed_states = args[1][1..args[1].len()-1].replace(",", "").split(" ").filter_map(|s| s.parse::<f64>().ok()).collect::<Vec<_>>();

    let target_pose = args[2][1..args[2].len()-1].replace(",", "").split(" ").filter_map(|s| s.parse::<f64>().ok()).collect::<Vec<_>>();

    g.pos_goals.push( Vector3::new(target_pose[0], target_pose[1], target_pose[2]) );
    let tmp_q = Quaternion::new(target_pose[6], target_pose[3], target_pose[4], target_pose[5] );
    g.quat_goals.push( UnitQuaternion::from_quaternion(tmp_q) );
    // println!("{:?}", args[3]);
    let info_file_path: String = args[3].clone();
    let mut r = librelaxed_ik::RelaxedIK::from_yaml_path(info_file_path, 1);
    r.vars.xopt = g.seed_states.clone();
    r.vars.prev_state = g.seed_states.clone();

    let x = r.solve(&g);

    
    println!("{:?}", x);
}