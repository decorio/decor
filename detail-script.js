document.addEventListener('DOMContentLoaded', function() {
    const detailTitle = document.getElementById('detail-title');
    const detailImageContainer = document.getElementById('detail-image-container');
    const detailBody = document.getElementById('detail-body');
    const relatedPostsContainer = document.getElementById('related-posts-container');
    const params = new URLSearchParams(window.location.search);
    const keywordFromQuery = params.get('q') || '';
    const keyword = keywordFromQuery.replace(/-/g, ' ').trim();

    function capitalizeEachWord(str) { 
        if (!str) return ''; 
        return str.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' '); 
    }

    // ▼▼▼ PERUBAHAN: hookWords, generateSeoTitle untuk Home Decor ▼▼▼
    function generateSeoTitle(baseKeyword) { 
        // Hook words baru untuk Home Decor
        const hookWords = ['Stunning', 'Chic', 'Creative', 'Affordable', 'Modern', 'Cozy', 'Elegant', 'Ultimate', 'Simple', 'Inspiring']; 
        const randomHook = hookWords[Math.floor(Math.random() * hookWords.length)]; 
        const randomNumber = Math.floor(Math.random() * (50 - 10 + 1)) + 10; // Tetap opsional
        const capitalizedKeyword = capitalizeEachWord(baseKeyword); 
        // Mengubah format judul menjadi lebih fokus pada desain/ide
        return `${randomHook} ${capitalizedKeyword} Design Ideas`; 
    }

    // Fungsi Spintax tetap sama
    function processSpintax(text) {
        const spintaxPattern = /{([^{}]+)}/g;
        while (spintaxPattern.test(text)) {
            text = text.replace(spintaxPattern, (match, choices) => {
                const options = choices.split('|');
                return options[Math.floor(Math.random() * options.length)];
            });
        }
        return text;
    }

    if (!keyword) { 
        detailTitle.textContent = 'Decor Idea Not Found'; 
        detailBody.innerHTML = '<p>Sorry, the requested home decor idea could not be found. Please return to the <a href="index.html">homepage</a>.</p>'; 
        if (relatedPostsContainer) { 
            relatedPostsContainer.closest('.related-posts-section').style.display = 'none'; 
        } 
        return; 
    }

    function populateMainContent(term) {
        const newTitle = generateSeoTitle(term);
        const capitalizedTermForArticle = capitalizeEachWord(term);
        document.title = `${newTitle} | HomeDecorSpot`; // Mengubah nama blog
        detailTitle.textContent = newTitle;

        // ▼▼▼ imageUrl TIDAK DIRUBAH (sesuai permintaan) ▼▼▼
        const imageUrl = `https://tse1.mm.bing.net/th?q=${encodeURIComponent(term)}&w=800&h=1200&c=7&rs=1&p=0&dpr=1.5&pid=1.7`;
        detailImageContainer.innerHTML = `<img src="${imageUrl}" alt="${newTitle}">`;

        // ▼▼▼ PERUBAHAN: ARTIKEL BARU untuk Home Decor dengan format Spintax ▼▼▼
        const spintaxArticleTemplate = `
            <p>{Welcome|Hello, design enthusiasts|Greetings, home stylers} to our blog! {This time|In this feature|On this page}, we will {explore|share|discover} {gorgeous|inspiring|chic} ideas for styling your space with <strong>${capitalizedTermForArticle}</strong>.
            {Finding|Discovering} the {right|perfect|most cohesive} design for <strong>${capitalizedTermForArticle}</strong> {can sometimes be a challenge|requires an eye for detail|is often easier said than done}.
            {That's why|Therefore}, we've {curated|gathered|presented} {a variety of|several} of the {best concepts|most sought-after ideas} for {you|our loyal readers}.</p>

            <h3>{Key Elements|Main Focus|Crucial Details} in ${capitalizedTermForArticle} Design</h3>
            <p>To {achieve|create|pull off} the {best|most stylish|most comfortable} results with your <strong>${capitalizedTermForArticle}</strong>, there are {several things|a few key aspects} that {need your attention|you should focus on}.
            {From|Whether it's} the {color palette|selection of textures}, {furniture arrangement|lighting design}, to the {final accessories|wall art}, everything {plays a crucial role|is highly influential|contributes significantly}.
            {Let's look at|Here are} some {more detailed|specific} {ideas|concepts|inspirations}:</p>

            <h4>1. {The Perfect|Balanced|Harmonious} Color Palette</h4>
            <p>{The foundation of|The secret to} any great room is its colors.
            For <strong>${capitalizedTermForArticle}</strong>, {you might consider|try using} {a monochromatic scheme with pops of color|warm neutrals with bold accents|cool tones for a calming effect} to {create|achieve} a mood that is {serene and inviting|energetic and vibrant|sophisticated and elegant}.</p>

            <h4>2. {Essential|The Right|Proper} Furniture Placement</h4>
            <p>{Beyond the beautiful pieces, your layout|Not just about the items, your arrangement} must also be {up to the task|considered}.
            {Choose|Select} furniture placement that {not only maximizes space|is suitable for} the <strong>${capitalizedTermForArticle}</strong> but also {ensures a good flow|is practical and functional}.
            {For instance|For example}, a {well-defined focal point|strategic use of area rugs|balanced conversational grouping} can be a {game-changer|designer's best friend}.</p>

            <h4>3. {Mastering|The Art of|Perfecting} Texture and Layering</h4>
            <p>{The right textures can|Proper layering techniques} {elevate your space|make all the difference}.
            {Consider combining|Pair different materials} like {soft velvets, rustic woods, and shiny metals|linen throws, woven baskets, and glass accessories}.
            This {creates layers of visual interest and comfort|adds a professional touch} to your <strong>${capitalizedTermForArticle}</strong>.</p>

            <h4>4. {Thoughtful|Balanced|Bold} Lighting Design</h4>
            <p>{Don't underestimate|Never forget} the power of light. {Ambient, task, and accent lighting|Layered lighting sources} {add depth, complexity, and balance|are essential for a complete design}.
            {Opt for|Choose} fixtures and lamp styles that {complement|enhance} your main <strong>${capitalizedTermForArticle}</strong> theme.</p>
			
			<h4>5. {Appetizing|Beautiful|Creative} Accessories & Styling</h4>
            <p>{Bare shelves are a missed opportunity|A room isn't finished until it's styled}.
            {A thoughtful arrangement of books, a collection of unique vases, or a set of framed prints|Color contrast, varied heights, and elegant display pieces} can {serve as a focal point|add a touch of class}.
            Good styling also {makes the room feel more personal|enhances the lived-in experience}.</p>

            <h4>6. {Healthy|Biophilic|Natural} Touches (Plants)</h4>
            <p>{Delicious design can also be healthy|Good style doesn't have to be cold}.
            {Whether it's a large potted plant, a simple succulent, or a vase of fresh flowers|From incorporating natural light to using wooden elements}, a natural touch {can make you feel good about where you're living|instantly boosts the air quality and mood}.
            This is a simple yet effective <strong>${capitalizedTermForArticle}</strong> trick.</p>

            <h4>7. {Smart|Efficient|Savvy} Storage Solutions</h4>
            <p>{A well-planned room is an organized room|Clutter can ruin a good design}.
            {Integrate smart storage solutions|Choose pieces that offer hidden functionality}.
            {Think built-in shelving, multi-purpose furniture, or stylish storage baskets|Consider wall-mounted units, ottomans with storage, or organizational inserts} to keep things {organized and stress-free|neat and tidy}.</p>

            <h4>8. {Add|A Dash of|Your} Personal Flair (Artwork)</h4>
            <p>{Finally, make the design yours|The final step is to add a personal touch}.
            {Incorporate pieces that tell your story|Showcase your unique taste}. {This could be a treasured family heirloom, a vintage flea market find, a piece of abstract art, or a DIY project|Think a special textile from your travels, a regional craftsman's work, or a cherished photo gallery}.
            These details make your <strong>${capitalizedTermForArticle}</strong> {truly unique|one-of-a-kind}.</p>

            <h3>{Conclusion|Final Thoughts|Wrapping It Up}</h3>
            <p>{So there you have it|And that's a wrap}—several {ideas and inspirations|gorgeous concepts|tips and tricks} for styling your space with <strong>${capitalizedTermForArticle}</strong> that {you can try|can serve as your guide in the design process}.
            {Remember, the key is|The most important thing to remember is} {creativity and trusting your personal style|being bold and experimenting with arrangement}.
            {Don't be afraid to|Feel free to} {mix and match|combine} different elements to {achieve|create} a final look that {truly|fully} {represents your style|satisfies your visual cravings}.</p>

            <p>{Happy decorating|Enjoy your beautiful home}!</p>
        `;

        // Proses Spintax dan tampilkan hasilnya
        detailBody.innerHTML = processSpintax(spintaxArticleTemplate);
    }

    // ▼▼▼ generateRelatedPosts TIDAK DIRUBAH (sesuai permintaan) ▼▼▼
    function generateRelatedPosts(term) {
        const script = document.createElement('script');
        script.src = `https://suggestqueries.google.com/complete/search?jsonp=handleRelatedSuggest&hl=en&client=firefox&q=${encodeURIComponent(term)}`;
        document.head.appendChild(script);
        script.onload = () => script.remove();
        script.onerror = () => { relatedPostsContainer.innerHTML = '<div class="loading-placeholder">Could not load related recipes.</div>'; script.remove(); }
    }

    window.handleRelatedSuggest = function(data) {
        const suggestions = data[1];
        relatedPostsContainer.innerHTML = '';
        if (!suggestions || suggestions.length === 0) { relatedPostsContainer.closest('.related-posts-section').style.display = 'none'; return; }
        const originalKeyword = keyword.toLowerCase();
        let relatedCount = 0;
        suggestions.forEach(relatedTerm => {
            if (relatedTerm.toLowerCase() === originalKeyword || relatedCount >= 11) return;
            relatedCount++;
            const keywordForUrl = relatedTerm.replace(/\s/g, '-').toLowerCase();
            const linkUrl = `detail.html?q=${encodeURIComponent(keywordForUrl)}`;
            
            const imageUrl = `https://tse1.mm.bing.net/th?q=${encodeURIComponent(relatedTerm)}&w=600&h=900&c=7&rs=1&p=0&dpr=1.5&pid=1.7`;
            const newRelatedTitle = generateSeoTitle(relatedTerm);
            const card = `<article class="content-card"><a href="${linkUrl}"><img src="${imageUrl}" alt="${newRelatedTitle}" loading="lazy"><div class="content-card-body"><h3>${newRelatedTitle}</h3></div></a></article>`;
            relatedPostsContainer.innerHTML += card;
        });
        if (relatedCount === 0) { relatedPostsContainer.closest('.related-posts-section').style.display = 'none'; }
    };

    populateMainContent(keyword);
    generateRelatedPosts(keyword);
});
