import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    def test_init_expect_to_initialize_correctly(self):
        hero = Hero("Hero", 5, 100, 20)
        self.assertEqual(hero.username, "Hero")
        self.assertEqual(hero.level, 5)
        self.assertEqual(hero.health, 100)
        self.assertEqual(hero.damage, 20)

    def test_battle__if_enemy_has_hero_username__expect_to_raise(self):
        hero = Hero("Hero", 5, 100, 20)
        enemy = Hero("Hero", 5, 100, 20)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)

        self.assertIsNotNone(ex)
        expected_message = "You cannot fight yourself"
        self.assertEqual(expected_message, str(ex.exception))

    def test_battle__if_hero_hp_lower_or_equal_to_zero_expect_to_raise(self):
        hero = Hero("Hero", 5, 0, 20)
        enemy = Hero("Enemy", 5, 100, 20)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertIsNotNone(ex)
        expected_message = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected_message, str(ex.exception))

    def test_battle__if_enemy_hp_lower_or_equal_to_zero_expect_to_raise(self):
        hero = Hero("Hero", 5, 100, 20)
        enemy = Hero("Enemy", 5, 0, 20)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertIsNotNone(ex)
        expected_message = f"You cannot fight Enemy. He needs to rest"
        self.assertEqual(expected_message, str(ex.exception))

    def test_battle__expect_hero_to_lose(self):
        hero = Hero("Hero", 5, 100, 15)
        enemy = Hero("Enemy", 5, 100, 20)
        initial_hero_health = hero.health
        initial_hero_level = hero.level
        initial_hero_damage = hero.damage
        initial_enemy_health = enemy.health
        initial_enemy_level = enemy.level
        initial_enemy_damage = enemy.damage
        result = hero.battle(enemy)

        self.assertEqual(enemy.health, initial_enemy_health - 70)
        self.assertEqual(enemy.level, initial_enemy_level + 1)
        self.assertEqual(enemy.damage, initial_enemy_damage + 5)
        self.assertEqual(hero.health, 0)
        self.assertEqual(initial_hero_level, hero.level)
        self.assertEqual(initial_hero_damage, hero.damage)
        self.assertEqual(result, "You lose")

    def test_battle__expect_hero_to_win(self):
        hero = Hero("Hero", 5, 100, 20)
        enemy = Hero("Enemy", 4, 100, 20)
        initial_hero_health = hero.health
        initial_hero_level = hero.level
        initial_hero_damage = hero.damage
        initial_enemy_health = enemy.health
        initial_enemy_level = enemy.level
        initial_enemy_damage = enemy.damage
        result = hero.battle(enemy)

        self.assertEqual(hero.health, initial_hero_health - 75)

        self.assertEqual(hero.level, initial_hero_level + 1)
        self.assertEqual(hero.damage, initial_hero_damage + 5)
        self.assertEqual(enemy.health, 0)
        self.assertEqual(initial_enemy_level, enemy.level)
        self.assertEqual(initial_enemy_damage, enemy.damage)
        self.assertEqual(result, "You win")

    def test_battle_expect_to_draw(self):
        hero = Hero("Hero", 5, 100, 20)
        enemy = Hero("Enemy", 5, 100, 20)
        initial_hero_level = hero.level
        initial_hero_damage = hero.damage
        initial_enemy_level = enemy.level
        initial_enemy_damage = enemy.damage
        result = hero.battle(enemy)
        self.assertEqual(hero.health, 0)
        self.assertEqual(enemy.health, 0)
        self.assertEqual(initial_hero_level, hero.level)
        self.assertEqual(initial_hero_damage, hero.damage)
        self.assertEqual(initial_enemy_level, enemy.level)
        self.assertEqual(initial_enemy_damage, enemy.damage)
        self.assertEqual(result, "Draw")

    def test_str__expect_to_output_correctly(self):
        hero = Hero("Hero", 5, 100, 20)
        expected_message = f"Hero Hero: 5 lvl\n" \
                           f"Health: 100\n" \
                           f"Damage: 20\n"
        self.assertEqual(expected_message, str(hero))