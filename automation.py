import subprocess

def build_docker_image():
    """
    Membuat image Docker untuk aplikasi Flask.
    """
    print("Membuat Docker image...")
    subprocess.run(['docker', 'build', '-t', 'flask_app', '.'], check=True)
    print("Docker image berhasil dibuat.")

def run_docker_container():
    """
    Menjalankan container Docker dari image Flask.
    """
    print("Menjalankan Docker container...")
    subprocess.run(['docker', 'run', '-d', '-p', '5000:5000', 'flask_app'], check=True)
    print("Docker container berhasil dijalankan.")
    print("Aplikasi berjalan di http://localhost:5000")

if __name__ == "__main__":
    try:
        build_docker_image()
        run_docker_container()
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan: {e}")
