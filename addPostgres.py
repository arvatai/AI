from korvus import Collection, Pipeline
import asyncio

# Initialize the collection
collection = Collection(database_url="postgres://postgresml:@192.168.1.3:5433/postgresml", name="my_collection")

# Define the pipeline for semantic search
pipeline = Pipeline(
    "v1",
    {
        "text": {
            "splitter": {"model": "recursive_character"},
            "semantic_search": {
                "model": "Alibaba-NLP/gte-base-en-v1.5"  # Ensure compatibility
            },
        }
    },
)

# Sample data to insert into the collection
data_to_insert = [
    {"text": " Why are the paused campaigns getting enabled? When using the Dayparting strategy, it is important to note that any paused campaigns linked to this strategy will become enabled if a multiplier of  is set anywhere within the strategy. This is because a multiplier of 0x indicates that the campaigns, regardless of their current status, will be paused. When the multiplier is set to a value greater than 0, the campaigns will be enabled, regardless of their previous state. This is why paused campaigns linked to the Dayparting strategy may become enabled when the strategy is executed. It is important to keep this in mind when utilizing the Dayparting strategy and managing your paused campaigns."},
]

# Function to add data to the collection
async def add_data():
    try:
        await Collection.upsert_documents(data_to_insert, da)
        print("Data added successfully.")
    except Exception as e:
        print(f"An error occurred while adding data: {e}")

# Add the pipeline to the collection
async def add_pipeline():
    try:
        await collection.add_pipeline(pipeline)
        print("Pipeline added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the pipeline: {e}")

# Run the setup and data insertion
async def main():
    await add_pipeline()
    await add_data()

asyncio.run(main())
