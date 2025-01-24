"""Config flow for Ezlo HA Cloud."""

# import my_pypi_dependency

# from homeassistant.core import HomeAssistant
# from homeassistant.helpers import config_entry_flow

# from .const import DOMAIN


# async def _async_has_devices(hass: HomeAssistant) -> bool:
#     """Return if there are devices that can be discovered."""
#     devices = await hass.async_add_executor_job(my_pypi_dependency.discover)
#     return len(devices) > 0


# config_entry_flow.register_discovery_flow(DOMAIN, "Ezlo HA Cloud", _async_has_devices)

import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        """Show user setup form."""
        errors = {}

        if user_input is not None:
            # Validate the input and store data
            try:
                # Custom validation logic here
                await self.async_set_unique_id("user_authentication")
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title="Ezlo HA Cloud", data=user_input)
            except config_entries.ConfigEntryError:
                errors["base"] = "already_configured"
            except Exception as e:  # noqa: BLE001
                errors["base"] = str(e)

        # Specify items in the order they are to be displayed in the UI
        # data_schema = {
        #     vol.Required("username"): str,
        #     vol.Required("password"): str,
        # }

        data_schema = {
            vol.Required("sni_host"): str,
            vol.Required("sni_port"): int,
            vol.Required("end_host"): str,
            vol.Required("end_port"): int,
            vol.Required("fernet_token"): str,
        }

        # await self.async_set_unique_id("ezlo_user_data")

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(data_schema), errors=errors
        )

    async def async_step_finish(self, user_input=None):  # noqa: D102
        if not user_input:
            return self.async_show_form(step_id="finish")
        return self.async_create_entry(title="", data={})
