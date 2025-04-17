from flask import Flask, jsonify
from app import db
from models import Toy, HealthyFood

app = Flask(__name__)

@app.route('/seed-products')
def seed_products():
    try:
        # Seed the database with toy and food products
        toys = [
            Toy(
                name="Squeaky Bone Toy",
                description="Made with durable rubber, ideal for long play hours!",
                price=300,
                image_url="https://i5.walmartimages.com/asr/1799388e-fbb9-430a-9eb6-1fea2e7848ef_1.9625af5a5c028241f2aa454c0c2bfac0.jpeg?odnHeight=450&odnWidth=450&odnBg=ffffff"
            ),
            Toy(
                name="Plush Chew Toy",
                description="Soft, cute, and comforting—perfect for puppies.",
                price=250,
                image_url="https://img.buzzfeed.com/buzzfeed-static/static/2021-12/9/19/asset/03eb6ce1bc83/sub-buzz-4574-1639077087-10.jpg"
            ),
            Toy(
                name="Catnip Ball",
                description="Organic catnip-filled ball to keep your kitty entertained!",
                price=350,
                image_url="https://m.media-amazon.com/images/I/715K55Bv3BL._AC_SL1500_.jpg"
            ),
            Toy(
                name="Three Tier Cat Tower",
                description="Let's the cat enjoy more",
                price=500,
                image_url="https://i5.walmartimages.com/asr/104f0791-02c4-4ba6-b5fd-64ee9bee9d50_1.4c656d194183b087ca4556da7669d921.jpeg"
            )
        ]

        foods = [
            HealthyFood(
                name="Premium Dry Kibble",
                description="High-protein, grain-free kibble made with real chicken and sweet potato. Great for all dog breeds.",
                price=500,
                image_url="https://thumbs.dreamstime.com/b/dry-kibble-dog-food-metal-bowl-wooden-table-91819272.jpg"
            ),
            HealthyFood(
                name="Gourmet Wet Cat Meals",
                description="Delicious tuna and salmon medley in gravy. Rich in omega-3 for shiny fur and healthy skin.",
                price=100,
                image_url="https://hip2save.com/wp-content/uploads/2020/07/cat-eating-wet-cat-food.jpg?resize=1024%2C538&strip=all?w=700&strip=all"
            ),
            HealthyFood(
                name="Homestyle Dog Meals",
                description="Human-grade ingredients slow cooked with veggies, rice, and lean meat. A wholesome dinner treat!",
                price=1000,
                image_url="https://th.bing.com/th/id/OIP.TOTc_DOLDzEJYo5XLBkuoQHaHa?rs=1&pid=ImgDetMain"
            ),
            HealthyFood(
                name="Starter Puppy Mix",
                description="Nutritious formula specially developed for growing puppies of all breeds.",
                price=499,
                image_url="https://http2.mlstatic.com/D_NQ_NP_871354-MLA43714550129_102020-F.jpg"
            ),
            HealthyFood(
                name="Tuna Crunchies",
                description="Crunchy and delicious tuna-flavored treats, enriched with vitamins and minerals.",
                price=199,
                image_url="https://th.bing.com/th/id/OIP.IA7FxXY8mjlG-KKlfomMYQHaLZ?rs=1&pid=ImgDetMain"
            )
        ]

        db.session.add_all(toys + foods)
        db.session.commit()

        return jsonify({"message": "Products seeded successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
