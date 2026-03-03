export const isTauriRuntime = () => {
  if (typeof window === 'undefined') {
    return false
  }

  return Boolean(window.__TAURI__ || window.__TAURI_INTERNALS__)
}
