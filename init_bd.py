from models import Base, engine

# Recreate tables with updated schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print("✅ Database reset with 'embedding' column.")
