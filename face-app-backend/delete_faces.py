from app import app, db, Face

# Use app context to allow DB session operations
with app.app_context():
    try:
        # Delete all face records
        db.session.query(Face).delete()
        db.session.commit()
        print("✅ All records from Face table deleted successfully.")
    except Exception as e:
        print(f"❌ Error: {e}")
