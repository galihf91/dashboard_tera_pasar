    # --- Kartu info pasar terpilih (versi ungu elegan) ---
    if ('nama_pasar' in df.columns) and (nama_pasar != "(Semua)"):
        info = df.loc[df['nama_pasar'] == nama_pasar].head(1)
        if not info.empty:
            nama = info['nama_pasar'].iat[0]
            alamat = info['alamat'].iat[0] if 'alamat' in info.columns else "Alamat tidak tersedia"
            kecamatan = info['kecamatan'].iat[0] if 'kecamatan' in info.columns else "–"

            st.markdown("---")
            st.markdown(
                f"""
                <div style="
                    background-color:#f3e8ff;              /* ungu pastel */
                    padding:14px 16px;
                    border-radius:12px;
                    border-left:5px solid #8000FF;         /* garis tepi ungu */
                    box-shadow:0px 1px 4px rgba(0,0,0,0.15);
                    margin-top:10px;
                    ">
                    <h4 style="margin-bottom:6px; color:#4B0082; font-size:16px;">
                        🏪 {nama}
                    </h4>
                    <p style="margin:2px 0; font-size:13px; color:#222;">
                        <b>Kecamatan:</b> {kecamatan}<br>
                        <b>Alamat:</b> {alamat}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
