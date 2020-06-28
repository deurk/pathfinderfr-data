#!/usr/bin/python3
# -*- coding: utf-8 -*-


# tables de correspondances
TARGETS = {
  "CA": { 'id': "ac", "subtargets": {
    "Générique": "ac",
    "Armure": "aac",
    "Bouclier": "sac",
    "Armure naturelle": "nac"
  }},
  "Jets d'attaque": { 'id': "attack", "subtargets": {
    "Tous": "attack",
    "Corps-à-corps": "mattack",
    "Distance": "rattack"
  }},
  "Dégâts": { 'id': "damage","subtargets": {
    "Tous": "damage",
    "Dégâts de l'arme": "wdamage",
    "Dégâts du sort": "sdamage"
  }},
  "Score de caractéristique": { 'id': "ability", "subtargets": {
    "Force": "str",
    "Dextérité": "dex",
    "Constitution": "con",
    "Intelligence": "int",
    "Sagesse": "wis",
    "Charisme": "cha"
  }},
  "Jets de sauvegarde": { 'id': "savingThrows", "subtargets": {
    "Tous": "allSavingThrows",
    "Vigueur": "ref",
    "Réflexes": "fort",
    "Volonté": "will"
  }},
  "Compétences": { 'id': "skills","subtargets": {
    "Toutes": "skills",
    "Basées sur la Force": "strSkills",
    "Basées sur la Dextérité": "dexSkills",
    "Basées sur la Constitution": "conSkills",
    "Basées sur l'Intelligence": "intSkills",
    "Basées sur la Sagesse": "wisSkills",
    "Basées sur le Charisme": "chaSkills"
  }},
  "Compétence spécifique": { 'id': "skill","subtargets": {
    "Acrobaties": "skill.acr",
    "Art de la magie": "skill.spl",
    "Artisanat": "skill.crf",
    "Artistry": "skill.art",
    "Bluff": "skill.blf",
    "Connaissances (Exploration souterraine)": "skill.kdu",
    "Connaissances (Folklore local)": "skill.klo",
    "Connaissances (Géographie)": "skill.kge",
    "Connaissances (Histoire)": "skill.khi",
    "Connaissances (Ingénierie)": "skill.ken",
    "Connaissances (Mystères)": "skill.kar",
    "Connaissances (Nature)": "skill.kna",
    "Connaissances (Noblesse)": "skill.kno",
    "Connaissances (Plans)": "skill.kpl",
    "Connaissances (Religion)": "skill.kre",
    "Déguisement": "skill.dis",
    "Diplomatie": "skill.dip",
    "Discrétion": "skill.ste",
    "Dressage": "skill.han",
    "Équitation": "skill.rid",
    "Escalade": "skill.clm",
    "Escamotage": "skill.slt",
    "Estimation": "skill.apr",
    "Évasion": "skill.esc",
    "Intimidation": "skill.int",
    "Lore": "skill.lor",
    "Linguistique": "skill.lin",
    "Natation": "skill.swm",
    "Perception": "skill.per",
    "Premiers Secours": "skill.hea",
    "Profession": "skill.pro",
    "Psychologie": "skill.en",
    "Représentation": "skill.prf",
    "Sabotage": "skill.dev",
    "Survie": "skill.sur",
    "Utilisation d'objets magiques": "skill.umd",
    "Vol": "skill.fly"
  }},
  "Tests de caractéristique": { 'id': "abilityChecks","subtargets": {
    "Tous": "allChecks",
    "Test de Force": "strChecks",
    "Test de Dextérité": "dexChecks",
    "Test de Constitution": "conChecks",
    "Test de Intelligence": "intChecks",
    "Test de Sagesse": "wisChecks",
    "Test de Charisme": "chaChecks"
  }},
  "Vitesse": { 'id': "speed", "subtargets": {
    "Toutes": "allSpeeds",
    "Vit. Base": "landSpeed",
    "Vit. Escalade": "climbSpeed",
    "Vit. Natation": "swimSpeed",
    "Vit. Creuser": "burrowSpeed",
    "Vit. Vol": "flySpeed"
  }},
  "Div.": { 'id': "misc", "subtargets": {
    "BBA": "cmb",
    "DMD": "cmd",
    "Initiative": "init",
    "Points de vie": "mhp",
    "Blessure": "wounds",
    "Vigueur": "vigor"
  }}
}

TYPES = {
  "Non-typé": "untyped",
  "Alchimique": "alchemical",
  "Altération": "enh",
  "Altération à l'armure": "enh",
  "Altération à l'armure naturelle": "enh",
  "Altération au bouclier": "enh",
  "Aptitude": "competence",
  "Armure": "base",
  "Armure naturelle": "base",
  "Bouclier": "base",
  "Chance": "luck",
  "Esquive": "dodge",
  "Inné": "inherent",
  "Intuition": "insight",
  "Moral": "morale",
  "Parade": "deflection",
  "Résistance": "resist",
  "Taille": "size"
}


#
# cette fonction crée un nouveau "buff" basé sur la structure de pf1
#
def createChange(formula, target, subtarget, type):
  if not target in TARGETS:
    print("Invalid target '%s'" % target)
    exit(1)
  target = TARGETS[target]
  
  if not subtarget in target["subtargets"]:
    print("Invalid subtarget '%s'" % subtarget)
    exit(1)
  subtarget = target["subtargets"][subtarget]
  
  if not type in TYPES:
    print("Invalid bonus type '%s'" % type)
    exit(1)
  type = TYPES[type]
  
  changes = {
    'formula': formula,
    'priority': 0,
    'target': target['id'],
    'subTarget': subtarget,
    'modifier': type
  }
  return changes;
