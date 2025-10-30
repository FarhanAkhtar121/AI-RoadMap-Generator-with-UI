import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { fileURLToPath } from "node:url";

const BACKEND = "https://ai-roadmap-generator-with-ui.onrender.com";
const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
  server: {
    proxy: {
      "/api": { target: BACKEND, changeOrigin: true, secure: true },
      "/output": { target: BACKEND, changeOrigin: true, secure: true },
    },
  },
});