// Reminder: since there is a GitHub limit of 100 megs, remember to: install npm i puppeteer BUT not in the same directory as the project

const puppeteer = require('puppeteer');

(async () => {
	const browser = await puppeteer.launch();
	const page = await browser.newPage();
	await page.goto('http://www.musimatic.net');	
	page.setViewport({width: 1920, height: 1080});
	await page.screenshot({path: 'musimaticWebpage.png'});

	await browser.close();

})();
