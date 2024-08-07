DROP VIEW IF EXISTS "community_profile_per_community_view";
CREATE OR REPLACE VIEW "community_profile_per_community_view" AS  SELECT DISTINCT
communities_community_profile.community_id,
communities_community_community.created AS joined,
communities_community_community."name" AS community_name,
communities_community_community.uuid AS community_uuid,
communities_profiles_profile.uuid,
communities_profiles_profile.profile_id,
communities_profiles_profile.created AS profile_created,
communities_profiles_profile.updated AS profile_updated,
communities_profiles_profile.creator_id AS profile_creator,
communities_profiles_profile.last_seen,
communities_profiles_profile.age,
communities_profiles_profile."name",
communities_profiles_profile.status,
communities_profiles_profile.species,
communities_profiles_profile.introduction,
communities_profiles_profile."level",
communities_profiles_profile."max_HP",
communities_profiles_profile."HP",
communities_profiles_profile."max_MP",
communities_profiles_profile."max_STUN",
communities_profiles_profile."STUN",
communities_profiles_profile."SHIELD",
communities_profiles_profile."MP",
communities_profiles_profile."max_SHIELD",
communities_profiles_profile."max_STA",
communities_profiles_profile.slug,
communities_profiles_profile.pronouns,
communities_profiles_profile."STA",
communities_profiles_profile.avatar,
communities_profiles_profile.gender,
communities_profiles_profile.posts,
communities_profiles_profile.views,
communities_profiles_profile.nodes,
communities_profiles_profile.archived,
communities_profiles_profile.blocked,
communities_profiles_profile.frozen,
communities_profiles_profile."system",
communities_profiles_profile.creator_id,
communities_profiles_profile.dynapage_id
FROM
communities_community_profile
INNER JOIN
communities_community_community
ON
communities_community_profile.community_id = communities_community_community.uuid
INNER JOIN
communities_profiles_profile
ON
communities_community_profile.profile_id = communities_profiles_profile.uuid
WHERE
communities_profiles_profile.placeholder = false;



DROP VIEW IF EXISTS communities_community_sidebar_view;

CREATE VIEW communities_community_sidebar_view AS SELECT
	communities_community_sidebar.uuid,
	communities_community_sidebar.application_mode,
	communities_community_sidebar."module",
	communities_community_sidebar.sidebar_class,
	communities_community_sidebar."ordering",
	communities_community_sidebar.active,
	communities_community_sidebar.community_id
FROM
	communities_community_sidebar;


DROP VIEW IF EXISTS communities_community_per_profile_dashboard_view;
CREATE VIEW communities_community_per_profile_dashboard_view AS SELECT
	communities_community_community_profile_dashboard_roles."id",
	communities_community_community_profile_dashboard_roles.active,
	communities_community_community_profile_dashboard_roles.community_id,
	communities_community_community_profile_dashboard_roles.profile_id,
	communities_community_community_dashboard_type."type",
	communities_community_community_dashboard_type.created,
	communities_community_community_dashboard_type.updated,
	communities_community_community_dashboard_type."name"
FROM
	communities_community_community_dashboard_type
	INNER JOIN
	communities_community_community_profile_dashboard_roles
	ON
		communities_community_community_dashboard_type.uuid = communities_community_community_profile_dashboard_roles.type_id;


DROP VIEW IF EXISTS communities_community_registry_page_view;
CREATE OR REPLACE VIEW communities_community_registry_page_view AS SELECT
    communities_community_registry.uuid as id,
	core_dynapages_page.page_id,
	core_dynapages_page.slug,
	core_dynapages_page.label,
	core_dynapages_page."system",
	core_dynapages_page.template_id,
	communities_community_registry."key",
	communities_community_registry."name",
	communities_community_registry.text_value,
	communities_community_registry.community_id,
	communities_community_registry.grouping_key,
	core_dynapages_page.creator_id
FROM
	core_dynapages_page
	INNER JOIN
	communities_community_registry
	ON
		core_dynapages_page.page_id = communities_community_registry.uuid_value
WHERE
    communities_community_registry.foreign_key_ref = 'core.dynapages.page';


CREATE RULE communities_community_registry_page_view_delete_rule AS ON DELETE TO communities_community_registry_page_view DO INSTEAD NOTHING;
