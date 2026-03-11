# def update_temporary_db():
#     app = create_app()
#     # app = create_app(TestConfig)
#     with app.app_context():
#         try:
#             station_details = DivPositions.query.all()
#             modify_station_details(station_details)
#         except Exception as e:
#             logging.critical(f"სკრიპტის შესრულების დროს შეცდომა: {e}")

# if __name__ == "__main__":
#     update_temporary_db()