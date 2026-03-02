// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            let exe_path = app.path().resource_dir().unwrap().join("app.exe");

            Command::new(exe_path)
                .spawn()
                .expect("Failed to start Flask");

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}