# cách 1:
# with open('historical_air_quality_2021_en.csv', 'r', encoding='UTF-8') as api_data_file:
#     print(api_data_file.readlines())

# Cách 2:
# Sử dụng thư viện csv:
# import csv
# with open('historical_air_quality_2021_en.csv', 'r', encoding='UTF-8') as api_data_file:
#     api_data = csv.reader(api_data_file)

#     for row in api_data:
#         print(row)


# Cách 3:
# Sử dụng thư viện Pandas
# Cài đặt thư viện : pip install pandas
import pandas

# api_data = pandas.read_csv('historical_air_quality_2021_en.csv')

# Lấy dữ liệu 1 cột
# station_id_data = api_data['Station ID']
# api_index_data = api_data['AQI index']
# print(station_id_data)
# print(api_index_data)

# Lấy dữ liệu của các hàng có Station ID = 8641
# us_embassy_station = api_data[ api_data['Station ID'] == 8641 ]
# print(us_embassy_station)

# Lấy dữ liệu theo các cột nhất định
cac_cot_muon_hien_thi = ['Station ID', 'Station name',
                         'AQI index', 'Temperature', 'Data Time S']
du_lieu_tra_ve = pandas.read_csv(
    'historical_air_quality_2021_en.csv', usecols=cac_cot_muon_hien_thi)

# Chuyển toàn bộ dữ liệu của cột AQI index sang số, nếu không phải số chuyển thành NaN
du_lieu_tra_ve['AQI index'] = pandas.to_numeric(
    du_lieu_tra_ve['AQI index'], errors='coerce')
print(du_lieu_tra_ve['AQI index'])

# Tính trung bình chất lượng không khí trong năm (AQI index) - mean(skipna = True) là bỏ qua những hàng NaN
trung_binh_chat_luong_khong_khi_tai_ha_noi_nam_2021 = du_lieu_tra_ve['AQI index'].mean(
    skipna=True)
chi_so_aqi_lon_nhat_nam_2021 = du_lieu_tra_ve['AQI index'].max(skipna=True)
chi_so_aqi_be_nhat_nam_2021 = du_lieu_tra_ve['AQI index'].min(skipna=True)
print(trung_binh_chat_luong_khong_khi_tai_ha_noi_nam_2021)
print(chi_so_aqi_lon_nhat_nam_2021)
print(chi_so_aqi_be_nhat_nam_2021)

# Lấy ra các hàng hay các trạm có chất lượng không khí > 100
cac_tram_co_aqi_index_lon_hon_100 = du_lieu_tra_ve[
    du_lieu_tra_ve['AQI index'] > 100
]

print(cac_tram_co_aqi_index_lon_hon_100)
