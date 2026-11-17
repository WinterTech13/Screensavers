using System;
using System.Diagnostics;
using System.IO;

namespace Screensaver {
    class Program {
        static void Main(string[] args) {
            string mode = "/s";
            if (args.Length > 0) {
                mode = args[0].ToLower().Trim().Substring(0, 2);
            }

            switch(mode) {
                case "/s":
                    Run();
                    break;
                case "/c":
                    break;
                case "/p":
                    break;
            }
        }

        static void Run() {
            string fileName = BuildConfig.ScriptFile;
            string currentDir = BuildConfig.CurrentDir;
            string scriptPath = Path.Combine(currentDir, fileName);
            string pythonPath = Path.Combine(Path.Combine(currentDir, "Scripts"), "pythonw.exe");
            
            var psi = new ProcessStartInfo {
                FileName = pythonPath,
                Arguments = string.Format("\"{0}\"", scriptPath),
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using (Process proc = Process.Start(psi)) {
                if (proc != null) {
                    proc.WaitForExit();
                }
            }
        }
    }
}