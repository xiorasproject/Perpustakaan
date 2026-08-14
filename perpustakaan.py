username = "admin"
password = "12345"
berhasil_login = False


# LOGIN
print("=====================================================")
print("   SELAMAT DATANG DI SISTEM INFORMASI PERPUSTAKAAN   ")
print("=====================================================")

for percobaan in range(1, 4):

    print("\n----- LOGIN PUSTAKAWAN -----")

    usn = input("Username : ")
    pw = input("Password : ")

    if usn == username and pw == password:

        print("\n[V] Login berhasil! Selamat bertugas.")
        berhasil_login = True
        break

    else:

        print("[X] Username atau password salah.")
        print(f"Percobaan ke-{percobaan} dari 3.")

if not berhasil_login:

    print("\nAnda di blokir dari program karena gagal login selama 3 kali.")

else:

    # INPUT DATA BUKU
    print("\n----- INPUT DATA BUKU -----")
    print("Silakan masukkan buku-buku yang akan dikelola.")

    while True:

        try:

            jumlah = int(input("Masukkan jumlah buku (minimal 3): "))

            if jumlah >= 3:
                break

            else:
                print("[!] Jumlah buku minimal 3.")

        except ValueError:

            print("[!] Masukkan jumlah dalam bentuk angka.")


    daftar_buku = []

    for i in range(jumlah):

        judul = input(f"Masukkan judul buku ke-{i + 1}: ")

        daftar_buku.append(judul)


    print("\n[V] Daftar buku berhasil disimpan di sistem.")
    print("Katalog Buku Saat Ini:", daftar_buku)


    # DATA AWAL STACK DAN QUEUE
    stack_buku = daftar_buku.copy()

    # Queue awalnya kosong- buku akan masuk ke Queue melalui POP dari Stack
    queue_buku = []


    # BUBBLE SORT
    def bubble_sort(data):

        # ASCENDING A-Z
        asc = data.copy()

        for i in range(len(asc)):

            for j in range(0, len(asc) - i - 1):

                if asc[j].lower() > asc[j + 1].lower():

                    asc[j], asc[j + 1] = asc[j + 1], asc[j]


        print("\n----- HASIL SORTING ASCENDING (A-Z) -----")

        print(asc)

        # DESCENDING Z-A
        desc = data.copy()

        for i in range(len(desc)):

            for j in range(0, len(desc) - i - 1):

                if desc[j].lower() < desc[j + 1].lower():

                    desc[j], desc[j + 1] = desc[j + 1], desc[j]


        print("\n----- HASIL SORTING DESCENDING (Z-A) -----")

        print(desc)


    # SEQUENTIAL SEARCH
    def sequential_search(data):

        cari = input("\nMasukkan judul buku yang ingin dicari: ")

        ditemukan = False

        for i in range(len(data)):

            if data[i].lower() == cari.lower():

                print(f"[V] Buku '{data[i]}' ditemukan pada indeks ke-{i}.")

                ditemukan = True
                break


        if not ditemukan:

            print(f"\n[X] Maaf, buku '{cari}' tidak ditemukan di perpustakaan.")


    # STACK TUMPUKAN PENGEMBALIAN BUKU
    def menu_stack():

        while True:

            print("\n========================================")
            print("       TUMPUKAN PENGEMBALIAN BUKU")
            print("              STACK - LIFO")
            print("========================================")

            print("\nData Stack Saat Ini:")

            if len(stack_buku) == 0:

                print("[]")

            else:

                print(stack_buku)


            print("\n1. Tambah Buku yang Dikembalikan (Push)")
            print("2. Proses Buku Teratas (Pop)")
            print("3. Exit")

            pilihan = input("\nMasukkan pilihan (1/2/3): ")


            # PUSH
            if pilihan == "1":

                judul = input(
                    "\nMasukkan judul buku yang baru dikembalikan: "
                )

                stack_buku.append(judul)

                print(
                    f"\n[V] Buku '{judul}' berhasil "
                    "ditambahkan ke Stack."
                )

                print("Isi Stack:", stack_buku)


            # POP
            elif pilihan == "2":

                if len(stack_buku) == 0:

                    print(
                        "\n[!] Stack kosong. "
                        "Tidak ada buku yang dapat diproses."
                    )

                else:

                    # Mengambil buku paling atas
                    judul = stack_buku.pop()

                    print(
                        f"\n[V] Buku '{judul}' "
                        "berhasil diproses dari Stack."
                    )

                    print("Sisa Stack:", stack_buku)


                    # Buku hasil POP masuk ke Queue
                    queue_buku.append(judul)

                    print(
                        f"[V] Buku '{judul}' "
                        "otomatis masuk ke Queue pemeriksaan."
                    )

                    print("Isi Queue:", queue_buku)


            # EXIT
            elif pilihan == "3":

                print("\n[V] Keluar dari menu Stack.")

                break


            else:

                print("\n[X] Pilihan tidak valid.")


    # QUEUE ANTREAN PEMERIKSAAN BUKU
    def menu_queue():

        while True:

            print("\n========================================")
            print("        ANTREAN PEMERIKSAAN BUKU")
            print("              QUEUE - FIFO")
            print("========================================")

            print("\nData Queue Saat Ini:")

            if len(queue_buku) == 0:

                print("[]")

            else:

                print(queue_buku)

            print("\n1. Tambah Buku ke Antrean Pemeriksaan (Enqueue)")
            print("2. Proses Buku Terdepan (Dequeue)")
            print("3. Exit")

            pilihan = input("\nMasukkan pilihan (1/2/3): ")


            # ENQUEUE
            if pilihan == "1":

                judul = input(
                    "\nMasukkan judul buku yang akan diperiksa: "
                )

                queue_buku.append(judul)

                print(
                    f"\n[V] Buku '{judul}' berhasil "
                    "ditambahkan ke Queue."
                )

                print("Isi Queue:", queue_buku)



            # DEQUEUE
            elif pilihan == "2":

                if len(queue_buku) == 0:

                    print(
                        "\n[!] Queue kosong. "
                        "Tidak ada buku yang dapat diproses."
                    )

                else:

                    # Mengambil buku paling depan
                    judul = queue_buku.pop(0)

                    print(
                        f"\n[V] Buku '{judul}' "
                        "berhasil diproses dari Queue."
                    )

                    print("Sisa Queue:", queue_buku)


            # EXIT
            elif pilihan == "3":

                print("\n[V] Keluar dari menu Queue.")

                break

            else:

                print("\n[X] Pilihan tidak valid.")


    # MENU UTAMA
    while True:

        print("\n========================================")
        print("          DASHBOARD PERPUSTAKAAN")
        print("========================================")

        print("1. Susun Katalog Buku (Bubble Sort)")
        print("2. Cari Judul Buku (Sequential Search)")
        print("3. Tumpukan Pengembalian Buku (Stack)")
        print("4. Antrean Pemeriksaan Buku (Queue)")
        print("5. Keluar Aplikasi (Exit)")

        print("========================================")

        pilihan = input("Pilih menu pengoperasian (1-5): ")


        if pilihan == "1":
            bubble_sort(daftar_buku)

        elif pilihan == "2":
            sequential_search(daftar_buku)

        elif pilihan == "3":
            menu_stack()

        elif pilihan == "4":
            menu_queue()

        elif pilihan == "5":
            print("\n========================================")
            print("       SISTEM PERPUSTAKAAN DITUTUP")
            print("========================================")
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print(
                "\n[X] Pilihan tidak valid. "
                "Silakan masukkan angka 1-5."
            )