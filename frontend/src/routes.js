import VueRouter from 'vue-router'

import HomePage from "@/pages/HomePage";
import CharacterListPage from "@/pages/CharacterListPage";
import CharacterDetailPage from "@/pages/CharacterDetailPage";

const routes = [
    {path: '/', component: HomePage},
    {path: '/characters', component: CharacterListPage},
    {path: '/characters/:id', component: CharacterDetailPage}
]

const router = new VueRouter({
    routes // short for `routes: routes`
})

export default router
