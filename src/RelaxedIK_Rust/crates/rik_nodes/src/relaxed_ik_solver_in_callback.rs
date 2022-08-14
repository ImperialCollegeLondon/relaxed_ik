use librelaxed_ik::utils_rust::subscriber_utils::EEPoseGoalsSubscriber;
use std::sync::{Arc, Mutex};
use rosrust;
use nalgebra::{Vector3, UnitQuaternion, Quaternion};

mod msg {
    rosrust::rosmsg_include!(relaxed_ik / EEPoseGoals, relaxed_ik / JointAngles);
}

fn main() {
    rosrust::init("relaxed_ik");

    println!("solver initialized!");

    // let mut r = librelaxed_ik::RelaxedIK::from_loaded(1);

    let arc = Arc::new(Mutex::new(Vec::new()));
    let arc2 = arc.clone();
    let _subscriber = rosrust::subscribe("/relaxed_ik/ee_pose_goals", 3, move |v: msg::relaxed_ik::EEPoseGoals| {
        let mut g = EEPoseGoalsSubscriber::new();
        // g.seed_states = Vec::new();
        // g.pos_goals = Vec::new();
        // g.quat_goals = Vec::new();

        let num_poses = v.ee_poses.len();

        g.seed_states = v.seed_states.data;
        g.req_id = v.req_id;
        for i in 0..num_poses {
            g.pos_goals.push( Vector3::new(v.ee_poses[i].position.x, v.ee_poses[i].position.y, v.ee_poses[i].position.z) );
            let tmp_q = Quaternion::new(v.ee_poses[i].orientation.w, v.ee_poses[i].orientation.x, v.ee_poses[i].orientation.y, v.ee_poses[i].orientation.z);
            g.quat_goals.push( UnitQuaternion::from_quaternion(tmp_q) );
        }

        let mut r = librelaxed_ik::RelaxedIK::from_loaded(1);

        r.vars.xopt = g.seed_states.clone();
        r.vars.prev_state = g.seed_states.clone();
        // r.vars.prev_state2 = g.seed_states[0].clone();
        

        let x = r.solve(&g);

        let mut ja = msg::relaxed_ik::JointAngles::default();
        ja.req_id = g.req_id;
        for i in 0..x.len() {
            ja.angles.data.push(x[i]);
        }

        let mut js_to_send = arc2.lock().unwrap();
        js_to_send.push(ja);
        

    });
    let publisher = rosrust::publish("/relaxed_ik/joint_angle_solutions", 3).unwrap();

    let rate1 = rosrust::rate(100.);
    while arc.lock().unwrap().is_empty() {rate1.sleep();}

    let rate = rosrust::rate(10.);
    while rosrust::is_ok() {
        // let x = r.solve(&arc.lock().unwrap());
        // println!("{:?}", x);
        // println!("{:?}", r.vars.init_ee_positions);

        // let mut ja = msg::relaxed_ik::JointAngles::default();
        // for i in 0..x.len() {
        //     ja.angles.data.push(x[i]);
        // }

        // let mut js_to_send = arc.lock().unwrap();
        println!("{:?}", arc.lock().unwrap().len());

        let _msg = match arc.lock().unwrap().pop() {
            Some(x) => {publisher.send(x).ok();},
            None => {},
        };

        // for i in 0..js_to_send.len() {
        //     publisher.send(&js_to_send[i]).ok();
        // }

        // publisher.send(ja).ok();

        rate.sleep();
    }
}