function HideAll() {
	$("#pnl_menu").hide();
	$("#pnl_projects").hide();
	$("#pnl_skills").hide();
	$("#pnl_timeline").hide();
}

function ShowMenu() {
	HideAll();
	$("#pnl_menu").removeClass("faded");
	$("#pnl_menu").show();
}

function ShowProjects() {
	HideAll();
	ShowMenu();
	$("#pnl_menu").addClass("faded");
	$("#pnl_projects").show();
}

function ShowSkills() {
	HideAll();
	$("#pnl_skills").show();
}

function ShowTimeline() {
	HideAll();
	$("#pnl_timeline").show();
}
