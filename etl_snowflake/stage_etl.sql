USE DATABASE snowflake_db;

USE schema staging;

-- copy from csv files
copy INTO precipitations
FROM
    '@file_csv/USC00420849-BOULDER-precipitation-inch.csv.gz' file_format = (format_name = csv_records) on_error = 'skip_file';

copy INTO temperatures
FROM
    '@file_csv/USC00420849-temperature-degreeF.csv.gz' file_format = (format_name = csv_records) on_error = 'skip_file';

-- copy from json files
copy INTO covid_features
FROM
    '@file_json/yelp_academic_dataset_covid_features.json.gz' file_format = (format_name = json_records) on_error = 'skip_file';

copy INTO business_features
FROM
    '@file_json/yelp_academic_dataset_business.json.gz' file_format = (format_name = json_records) on_error = 'skip_file';

copy INTO checkins
FROM
    '@file_json/yelp_academic_dataset_checkin.json.gz' file_format = (format_name = json_records) on_error = 'skip_file';

copy INTO reviews
FROM
    '@file_json/yelp_academic_dataset_review.json.gz' file_format = (format_name = json_records) on_error = 'skip_file';

copy INTO tips
FROM
    '@file_json/yelp_academic_dataset_tip.json.gz' file_format = (format_name = json_records) on_error = 'skip_file';

copy INTO users
FROM
    '@file_json/yelp_academic_dataset_user.json.gz' file_format = (format_name = json_records) on_error = 'skip_file';