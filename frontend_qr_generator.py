import qrcode
import os
from PIL import Image, ImageDraw, ImageFont


def generate_frontend_qr():
    """Generate QR code that links to the frontend HTML file"""
    
    print("🔍 Checking for index.html file...")
    
    # Check if index.html exists in current directory
    if os.path.exists("index.html"):
        print("✅ Found index.html in current directory")
        # Use local HTTP server approach
        frontend_url = "http://localhost:8080/index.html"
        server_method = "Python HTTP Server"
    else:
        print("⚠️  index.html not found in current directory")
        # Use Flask backend approach
        frontend_url = "http://localhost:6969/frontend"
        server_method = "Flask Backend"
    
    print(f"📱 Creating QR code for: {frontend_url}")
    print(f"🔧 Recommended server method: {server_method}")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(frontend_url)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Resize to make it larger
    img = img.resize((300, 300), Image.Resampling.LANCZOS)
    
    # Create a new image with title
    final_img = Image.new('RGB', (350, 380), 'white')
    final_img.paste(img, (25, 25))
    
    # Add title text
    draw = ImageDraw.Draw(final_img)
    try:
        # Try to use a nice font
        font_title = ImageFont.truetype("Arial.ttf", 20)
        font_subtitle = ImageFont.truetype("Arial.ttf", 14)
    except:
        # Fallback to default font
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
    
    # Add title
    title_text = "Library Management System"
    subtitle_text = "Scan to access the library"
    
    # Get text bounds for centering
    title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=font_subtitle)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    
    # Draw text
    draw.text(((350 - title_width) // 2, 340), title_text, fill="black", font=font_title)
    draw.text(((350 - subtitle_width) // 2, 365), subtitle_text, fill="gray", font=font_subtitle)
    
    # Save the QR code
    final_img.save("library_frontend_qr.png")
    print("✅ Frontend QR code saved as 'library_frontend_qr.png'")
    print(f"📱 QR code links to: {frontend_url}")
    
    return frontend_url, server_method

def add_cse_books_to_database():
    """Add computer science books to the database"""
    import sqlite3
    
    # Computer Science books data
    cse_books = [
        {
            'isbn': '9780262033848',
            'title': 'Introduction to Algorithms',
            'author': 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein',
            'category': 'Computer Science',
            'publication_year': 2009,
            'description': 'Comprehensive introduction to algorithms and data structures',
            'copies': 5,
            'available': 4
        },
        {
            'isbn': '9780134494166',
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
            'author': 'Robert C. Martin',
            'category': 'Programming',
            'publication_year': 2008,
            'description': 'Best practices for writing clean, maintainable code',
            'copies': 3,
            'available': 2
        },
        {
            'isbn': '9780135957059',
            'title': 'The Pragmatic Programmer',
            'author': 'David Thomas, Andrew Hunt',
            'category': 'Programming',
            'publication_year': 2019,
            'description': 'Your journey to mastery in software development',
            'copies': 4,
            'available': 3
        },
        {
            'isbn': '9781449355739',
            'title': 'Designing Data-Intensive Applications',
            'author': 'Martin Kleppmann',
            'category': 'Database',
            'publication_year': 2017,
            'description': 'The big ideas behind reliable, scalable, and maintainable systems',
            'copies': 3,
            'available': 1
        },
        {
            'isbn': '9780596007126',
            'title': 'Head First Design Patterns',
            'author': 'Eric Freeman, Elisabeth Robson',
            'category': 'Software Engineering',
            'publication_year': 2004,
            'description': 'A brain-friendly guide to design patterns',
            'copies': 2,
            'available': 2
        },
        {
            'isbn': '9780134052502',
            'title': 'Operating System Concepts',
            'author': 'Abraham Silberschatz, Peter Baer Galvin, Greg Gagne',
            'category': 'Operating Systems',
            'publication_year': 2018,
            'description': 'Comprehensive introduction to operating systems',
            'copies': 4,
            'available': 3
        },
        {
            'isbn': '9780321573513',
            'title': 'Algorithms + Data Structures = Programs',
            'author': 'Niklaus Wirth',
            'category': 'Computer Science',
            'publication_year': 2004,
            'description': 'Classic text on algorithms and data structures',
            'copies': 2,
            'available': 1
        },
        {
            'isbn': '9780134685991',
            'title': 'Effective Java',
            'author': 'Joshua Bloch',
            'category': 'Programming',
            'publication_year': 2017,
            'description': 'Best practices for the Java programming language',
            'copies': 3,
            'available': 3
        },
        {
            'isbn': '9781593279509',
            'title': 'Eloquent JavaScript',
            'author': 'Marijn Haverbeke',
            'category': 'Web Development',
            'publication_year': 2018,
            'description': 'A modern introduction to programming with JavaScript',
            'copies': 4,
            'available': 2
        },
        {
            'isbn': '9780132350884',
            'title': 'Clean Architecture',
            'author': 'Robert C. Martin',
            'category': 'Software Architecture',
            'publication_year': 2017,
            'description': 'A craftsman\'s guide to software structure and design',
            'copies': 3,
            'available': 1
        },
        {
            'isbn': '9780596516178',
            'title': 'JavaScript: The Good Parts',
            'author': 'Douglas Crockford',
            'category': 'Web Development',
            'publication_year': 2008,
            'description': 'Unearthing the excellence in JavaScript',
            'copies': 2,
            'available': 0
        },
        {
            'isbn': '9780134494913',
            'title': 'Computer Systems: A Programmer\'s Perspective',
            'author': 'Randal E. Bryant, David R. O\'Hallaron',
            'category': 'Computer Systems',
            'publication_year': 2015,
            'description': 'How computer systems work from a programmer\'s perspective',
            'copies': 3,
            'available': 2
        },
        {
            'isbn': '9780136083405',
            'title': 'Computer Networking: A Top-Down Approach',
            'author': 'James Kurose, Keith Ross',
            'category': 'Networking',
            'publication_year': 2016,
            'description': 'Modern approach to computer networking',
            'copies': 4,
            'available': 4
        },
        {
            'isbn': '9780262046305',
            'title': 'Artificial Intelligence: A Modern Approach',
            'author': 'Stuart Russell, Peter Norvig',
            'category': 'Artificial Intelligence',
            'publication_year': 2020,
            'description': 'Comprehensive introduction to artificial intelligence',
            'copies': 5,
            'available': 3
        },
        {
            'isbn': '9781449373320',
            'title': 'Learning React',
            'author': 'Alex Banks, Eve Porcello',
            'category': 'Web Development',
            'publication_year': 2020,
            'description': 'Modern patterns for developing React apps',
            'copies': 3,
            'available': 2
        }
    ]
    
    try:
        # Connect to database
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        
        # Insert CSE books
        books_added = 0
        for book in cse_books:
            try:
                c.execute('''
                    INSERT OR IGNORE INTO books 
                    (isbn, title, author, category, publication_year, description, copies, available)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    book['isbn'],
                    book['title'],
                    book['author'],
                    book['category'],
                    book['publication_year'],
                    book['description'],
                    book['copies'],
                    book['available']
                ))
                if c.rowcount > 0:
                    books_added += 1
            except Exception as e:
                print(f"❌ Error adding book {book['title']}: {e}")
        
        conn.commit()
        conn.close()
        
        print(f"✅ Successfully added {books_added} new CSE books to the database!")
        print(f"📚 Total books attempted: {len(cse_books)}")
        
        if books_added < len(cse_books):
            print(f"ℹ️  {len(cse_books) - books_added} books were already in the database")
            
    except Exception as e:
        print(f"❌ Database error: {e}")

def create_simple_http_server_guide():
    """Create a guide for serving the HTML file"""
    guide = """
# 🌐 How to Serve Your HTML File

## Method 1: Python HTTP Server (Recommended)
# Navigate to your HTML file directory and run:
python3 -m http.server 8080

# Then your QR code will work with: http://localhost:8080/index.html

## Method 2: Node.js (if you have it)
# Install a simple server:
npm install -g http-server

# Run in your HTML directory:
http-server -p 8080

## Method 3: Use your Flask app to serve HTML
# Add this route to your app.py:

@app.route('/frontend')
def serve_frontend():
    with open('index.html', 'r') as file:
        return file.read()

# Then use: http://localhost:5000/frontend in your QR code

## Method 4: Upload to GitHub Pages (for permanent hosting)
# 1. Create a GitHub repository
# 2. Upload your index.html
# 3. Enable GitHub Pages in settings
# 4. Use the GitHub Pages URL in your QR code
"""
    
    with open('server_setup_guide.txt', 'w') as f:
        f.write(guide)
    print("📄 Server setup guide saved as 'server_setup_guide.txt'")

if __name__ == "__main__":
    print("🚀 Library Management System Setup")
    print("=" * 50)
    
    # Generate frontend QR code
    print("\n1️⃣  Generating QR code for frontend...")
    frontend_url, server_method = generate_frontend_qr()
    
    # Add CSE books to database
    print("\n2️⃣  Adding Computer Science books to database...")
    add_cse_books_to_database()
    
    # Create server guide
    print("\n3️⃣  Creating server setup guide...")
    create_simple_http_server_guide()
    
    print("\n" + "=" * 50)
    print("✅ Setup complete!")
    print(f"\n📱 QR Code created for: {frontend_url}")
    print(f"🔧 Recommended method: {server_method}")
    print("\n📋 Next steps:")
    
    if os.path.exists("index.html"):
        print("   Since index.html exists:")
        print("   1. Run: python3 -m http.server 8080")
        print("   2. Open: http://localhost:8080/index.html")
        print("   3. Or run your Flask app and visit: http://localhost:5000/frontend")
    else:
        print("   Since index.html is missing:")
        print("   1. Save the HTML code from Claude as 'index.html'")
        print("   2. Run your Flask app: python app.py")
        print("   3. Visit: http://localhost:6969/frontend")
    
    print("   4. Print and use the generated QR code!")
    print("   5. Test the new CSE books in your system!")